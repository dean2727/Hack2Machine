'''
File: Parser.py
Author: Dean Orenstein
Date: 04/07/2020
Section: 511
E-mail: dean27@tamu.edu

Description:
Parser class: reads file and unpacks each instruction into its underlying fields
'''

class Parser:
    # Constructor: opens input file and gets ready to parse it
    def __init__(self, fileName, updatedSymbolTable):
        # Error checking because file may not open
        try:
            self.ourFile = open(fileName, 'r')
        except IOError:
            print("Could not open file", fileName)
            sys.exit()
        # Other members: current line (command), symbol table, and counter (for label adding)
        self.command = self.ourFile.readline()
        self.tables = updatedSymbolTable
        self.n = 16

    # Returns true if theres more lines for the input file
    def hasMoreCommands(self):
        if self.command != '':
            return True
        else:
            return False

    # Reads the next line(s) in the file (used in the second pass)
    def advance(self):
        # If we cant read any more lines, close the file and return
        if not self.hasMoreCommands():
            self.ourFile.close()
            return ''

        #print("DEBUG: current command is", self.command)

        # If the command is not a comment or all whitespace
        if not self.command.isspace():
            # Strip white space before first character occurrence
            self.command = self.command.lstrip()
            # If the command is not a comment or a label (xxx)
            if not (self.command[0:2] == "//" or self.command[0] == "("):
                
                # Strip the whitespace away from the command and remove any comment after it
                command = self.command.strip()
                if "//" in command:
                    endPos = command.find("//")
                    command = command[0 : endPos]

                commandType = self.commandType(command)
                # If command type is L command, address is 0 (dont write to MyProg.hack)
                if commandType == "L_COMMAND":
                    address = 0

                # Else, if command type is A command
                elif commandType == "A_COMMAND":
                    # If xxx is a variable
                    if not command[1:].isdigit():
                        variable = command[1:]
                        # If its not in the symbol table, add to it and increment n
                        if not self.tables.contains(variable):
                            self.tables.addEntry(variable, self.n)
                            self.n += 1
                        # Address is found from the table
                        address = self.tables.getAddress(variable)
                    # Else, its a digit
                    else:
                        address = int(command[1:])
                    # Convert address to binary value (string)
                    address = str(bin(address))
                    # Remove the "0b" from the beginning
                    address = address[2:]
                    # Add any filler 0 bits
                    if len(address) < 16:
                        numZeros = 16 - len(address)
                        address = numZeros*"0" + address
                
                # Else, its a C command
                else:
                    comp = self.comp()
                    dest = self.dest()
                    jump = self.jump()
                    # return full binary string with the 3 mnemonics
                    address = "111" + comp + dest + jump
            
            # Address is 0 (dont write to MyProg.hack) if white space or comment
            else:
                address = 0
        else:
            address = 0

        # Read next line and return address
        self.command = self.ourFile.readline()
        return address

    # Returns what kind of command we have
    def commandType(self, command):
        # Return "A_COMMAND" if a-instruction
        #print("DEBUG: first char of command is", self.command[0])
        #print("DEBUG: rest of the command is", self.command[1:])
        if command[0] == "@":
            #print("DEBUG: WERE IN")
            return "A_COMMAND"

        # Return "C_COMMAND" if c-instruction
        if ";" in command or "=" in command:
            return "C_COMMAND"

        # Return "L_COMMAND" for (xxx))
        return "L_COMMAND"
    
    # Returns the symbol/decimal xxx of the current command @xxx
    def symbol(self):
        return self.command[1:].strip()
        
    # Returns the comp mnemonic (28 possibilities) of the current c-instruction
    def comp(self):
        # dest mnemonic present
        if "=" in self.command: 
            startPos = self.command.find("=") + 1
            # jump mnemonic present: get mnemonic between the = and ;
            if ";" in self.command:
                endPos = self.command.find(";")
                mnemonic = self.command[startPos : startPos-endPos]
            # no jump mnemonic present: remove any possible comment after the mnemonic then slice
            else:
                mnemonic = "".join(self.command.split())
                if "//" in mnemonic:
                    endPos = mnemonic.find("//")
                    mnemonic = mnemonic[0 : endPos]
                mnemonic = mnemonic[startPos:]
        # if no dest mnemonic present then a jump mnemonic must be present
        else:
            mnemonic = "".join(self.command.split())
            endPos = self.command.find(";")
            mnemonic = self.command[0 : endPos]

        # Look up mnemonic in table and return its binary string
        return self.tables.compTable[mnemonic]

    # Returns the dest mnemonic (8 possibilities) of the current c-instruction
    def dest(self):
        # Case where the dest portion is omitted from the instruction (return null -> "000")
        if "=" not in self.command:
            return "000"
        
        # Get the mnemonic by slicing, strip whitepace away
        length = self.command.find("=")
        mnemonic = self.command[0 : length].strip()

        # Look up mnemonic in table and return its binary string
        return self.tables.destTable[mnemonic]
    
    # Returns the jump mnemonic (8 possibilities) of the current c-instruction
    def jump(self):
        # Case where the jump portion isnt part of the instruction (return null -> "000")
        if ";" not in self.command:
            return "000"

        # Get the mnemonic by slicing, strip whitepace away, remove any comment after it
        startPos = self.command.find(";") + 1
        mnemonic = "".join(self.command.split())
        if "//" in mnemonic:
            endPos = mnemonic.find("//")
            mnemonic = mnemonic[0 : endPos]
        mnemonic = mnemonic[startPos:]

        # Look up mnemonic in table and return its binary string
        return self.tables.jumpTable[mnemonic]