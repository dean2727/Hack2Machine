'''
File: Assembler.py
Author: Dean Orenstein
Date: 04/07/2020
Section: 511
E-mail: dean27@tamu.edu

Description:
The content of this file takes an assembly file as input, converts 
the code to binary, and writes these codes to a new file
(We are assuming the assembly code is error free)
'''

# Importing sys lets us access the command-line arguments (just the .asm file in our case)
import sys


# Code class: translates each field into its corresponding binary value
# class Code:
#     def dest(self, mnemonic):
#         return SYMBOLS[mnemonic]
#     def comp(self, mnemonic):
#         return SYMBOLS[mnemonic]
#     def jump(self, mnemonic):
#         return SYMBOLS[mnemonic]


# SymbolTable class: manages the symbol table (Hack assembly language symbols)
class SymbolTable:
    # Constructor: creates new symbol table with the predefined symbols
    def __init__(self):
        self.table = {'R0':0, 'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5,
           'R6':6, 'R7':7, 'R8':8, 'R9':9, 'R10':10,
           'R11':11, 'R12':12, 'R13':13, 'R14':14, 'R15':15,
           "SCREEN":16384, "KBD":24576, 
           "SP":0, "LCL":1, "ARG":2, "THIS":3, "THAT":4}
        #self.highestAddr = 15  # Tracks the address of newest added label (start at R15)
    
    # Adds a symbol-address (key-value) pairing to the table
    def addEntry(self, symbol, address):
        table[symbol] = address

    # Returns true if the table already contains the symbol
    def contains(self, symbol):
        if symbol in table:
            return True
        else:
            return False

    # Return the address (integer) associated with the symbol
    def getAddress(self, symbol):
        return self.table[symbol]


# Parser class: reads file and unpacks each instruction into its underlying fields
class Parser:
    # Constructor: opens input file and gets ready to parse it
    def __init__(self, fileName):
        # Error checking because file may not open
        try:
            self.asmFile = open(fileName, 'r')
        except IOError:
            print("Could not open file", fileName)
            sys.exit()
        # Other members: currentLine, symbolTable, and code
        self.currentLine = self.asmFile.readline()
        self.command
        self.symbols = SymbolTable()
       
    # Destructor: closes the file
    # def __del__(self):
    #     self.asmFile.close()
    
    # Returns true if theres more lines for the input file
    def hasMoreCommands(self):
        if self.currentLine != '':
            return True
        else:
            return False

    # Reads the next line(s) in the file
    def advance(self):
        # If we cant read any more lines, close the file and return
        self.command = self.asmFile.readline()
        if self.command == '':
            print("Done! No more lines to read from asm file!")
            self.asmFile.close()
            return

        # Strip white space before first character occurrence
        self.command = self.command.lstrip()

        # If the command is not a comment or all whitespace
        if not (self.command.isspace() or self.command[0:2] == "//"):

            # To convert the int to its binary equivalent, we'll use bin(), e.g. bin(2) -> 0000000000000010
            # If a-instruction, get its symbol, check if in table (update if not),
            # return string of its value in binary
            if self.getCommandType(self.command) == "A_COMMAND":
                if not self.symbols.contains(self.symbol):
                    self.symbols.addEntry(self.symbol, )
                return str(bin(self.symbols.getAddress()))
            
            # If c-instruction, figure out mnemonics and get bits accordingly
            elif self.getCommandType(self.command) == "C_COMMAND":
                return "111" + self.comp + self.dest + self.jump
            
            # If label, get its symbol, check if in table (update if not), return string
            # of its value in binary
            elif self.getCommandType(self.command) == "L_COMMAND":

    # Returns what kind of command we have
    def getCommandType(self):
        # Return "A_COMMAND" if A-instruction
        if self.command[0] == "@":
            return "A_COMMAND"

        # Return "C_COMMAND" if C-instruction
        if ";" in self.command or "=" in self.command:
            return "C_COMMAND"

        # Return "L_COMMAND" for (<symbol>)
        if self.command[0] == "(" and self.command[-1] == ")":
            return "L_COMMAND"
    
    # Returns the symbol/decimal xxx of the current command @xxx or (xxx)
    def symbol(self):
        if self.command[0] == "@":
            return self.command[1:].strip()
        else:
            return self.command[1: len(self.command)-1].strip()
    
    # Returns the comp mnemonic (28 possibilities) of the current c-instruction
    def comp(self):
        instruction = "111"

        # Get the actual mnemonic first, starting by slicing the command
        if "=" in self.command:
            startPos = self.command.find("=") + 1
            if ";" in self.command:
                endPos = self.command.find(";")
                mnemonic = self.command[startPos: startPos - endPos]
            else:
                mnemonic = self.command[startPos: len(self.command) - startPos]
        else:
            length = self.command.find(";") - 1
            mnemonic = self.command[0: length]
        # Strip away any whitespace in the mnemonic
        mnemonic = "".join(mnemonic.split())

        # Now we can check each possibility
        if mnemonic == "0":
            instruction += "0101010"
        elif mnemonic == "1":
            instruction += "0111111"
        elif mnemonic == "-1":
            instruction += "0111010"
        elif mnemonic == "D":
            instruction += "0001100"
        elif mnemonic == "A":
            instruction += "0110000"
        elif mnemonic == "M":
            instruction += "1110000"
        elif mnemonic == "!D":
            instruction += "0001101"
        elif mnemonic == "!A":
            instruction += "0110001"
        elif mnemonic == "!M":
            instruction += "1110001"
        elif mnemonic == "-D":
            instruction += "0001111"
        elif mnemonic == "-A":
            instruction += "0110011"
        elif mnemonic == "-M":
            instruction += "1110011"
        elif mnemonic == "D+1":
            instruction += "0011111"
        elif mnemonic == "A+1":
            instruction += "0110111"
        elif mnemonic == "M+1":
            instruction += "1110111"
        elif mnemonic == "D-1":
            instruction += "0001110"
        elif mnemonic == "A-1":
            instruction += "0110010"
        elif mnemonic == "M-1":
            instruction += "1110010"
        elif mnemonic == "D+A":
            instruction += "0000010"
        elif mnemonic == "D+M":
            instruction += "1000010"
        elif mnemonic == "D-A":
            instruction += "0010011"
        elif mnemonic == "D-M":
            instruction += "1010011"
        elif mnemonic == "A-D":
            instruction += "0000111"
        elif mnemonic == "M-D":
            instruction += "1000111"
        elif mnemonic == "D&A":
            instruction += "0000000"
        elif mnemonic == "D&M":
            instruction += "1000000"
        elif mnemonic == "D|A":
            instruction += "0010101"
        elif mnemonic == "D|M":
            instruction += "1010101"

        return instruction

    # Returns the dest mnemonic (8 possibilities) of the current c-instruction
    def dest(self):
        # Case where the dest portion is omitted from the instruction (return null -> "000")
        if "=" not in self.command:
            return "000"
        
        # Get the mnemonic by slicing, strip whitepace away
        length = self.command.find("=") - 1
        mnemonic = self.command[0: length].strip()

        if mnemonic == "M":
            return "001"
        if mnemonic == "D":
            return "010"
        if mnemonic == "MD":
            return "011"
        if mnemonic == "A":
            return "100"
        if mnemonic == "AM":
            return "101"
        if mnemonic == "AD":
            return "110"
        if mnemonic == "AMD":
            return "111"
    
    # Returns the jump mnemonic (8 possibilities) of the current c-instruction
    def jump(self):
        # Case where the jump portion isnt part of the instruction (return null -> "000")
        if ";" not in self.command:
            return "000"

        # Get the mnemonic by slicing, strip whitepace away
        startPos = self.command.find(";") + 1
        mnemonic = self.command[startPos: len(self.command) - startPos].strip()

        if mnemonic == "JGT":
            return "001"
        if mnemonic == "JEQ":
            return "010"
        if mnemonic == "JGE":
            return "011"
        if mnemonic == "JLT":
            return "100"
        if mnemonic == "JNE":
            return "101"
        if mnemonic == "JLE":
            return "110"
        if mnemonic == "JMP":
            return "111"


# Main program
if __name__ == "__main__":
    # Create new Parser object with 2nd command-line arg
    fileName = sys.argv[1]
    asmParser = Parser(fileName)

    # Create 

    # First Pass: Read all commands, only paying attention to labels and
    # updating the symbol table


    # Restart reading and translating commands
    
