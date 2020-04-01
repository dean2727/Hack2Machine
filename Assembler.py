'''
File: Assembler.py
Author: Dean Orenstein
Date: 04/07/2020
Section: 511
E-mail: dean27@tamu.edu

Description:
The content of this file takes an assembly file as input, converts 
the code to binary, and writes these codes to a new file
'''

# Importing sys lets us access the command-line arguments (just the .asm file in our case)
import sys

# Global dictionary to hold certain Hack syntax and their values, start with pre-defined symbols
# To convert the int to its binary equivalent, we'll use bin(), e.g. bin(2) -> 0000000000000010
SYMBOLS = {'R0':0, 'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5,
           'R6':6, 'R7':7, 'R8':8, 'R9':9, 'R10':10,
           'R11':11, 'R12':12, 'R13':13, 'R14':14, 'R15':15,
           "SCREEN":16384, "KBD":24576, 
           "SP":0, "LCL":1, "ARG":2, "THIS":3, "THAT":4,
           # Now onto c-instruction mnemonics (string values make life easier)
           "M":"001", "D":"010", "MD":"011", "A":"100", "AM":"101", "AD":"110", "AMD":"111"} 

# Code class: contains methods that return binary translations of c-instruction mnemonics
class Code:
    def dest(self, mnemonic):
        return SYMBOLS[mnemonic]
    def comp(self, mnemonic):
        return SYMBOLS[mnemonic]
    def jump(self, mnemonic):
        return SYMBOLS[mnemonic]

# SymbolTable class: represents our symbols for the Hack assembly language
class SymbolTable:
    # Constructor: creates new empty symbol table
    def __init__(self):
        self.table = {}
    
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


# Parser class: parses our assembly file
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
        self.possibleCommand
        # self.symbols = SymbolTable()
       
    # Destructor: closes the file
    def __del__(self):
        self.asmFile.close()
    
    # Returns true if theres more lines for the input file
    def hasMoreCommands(self):
        if self.currentLine != '':
            return True
        else:
            return False

    # Reads the next line(s) in the file, setting 
    def advance(self):
        # If we cant read any more lines, close the file and return
        self.possibleCommand = self.asmFile.readline()
        if self.possibleCommand == '':
            print("Done! No more lines to read from asm file!")
            self.asmFile.close()
            return

        # Else, process this line
        while self.possibleCommand != '':
            # If its not a comment or all whitespace
            if not (self.possibleCommand.isspace() or self.possibleCommand.lstrip()[0:2] == "//"):
                # 

            # Read next command
            self.possibleCommand = self.asmFile.readline()

        # Close file and return
        self.asmFile.close()
        return

    # Returns what kind of command we have
    def getCommandType(self, command):
        # Return "A_COMMAND" if 
        if command.
    
    def symbol(self):
    
    def dest(self):
    
    def comp(self):
    
    def jump(self):


# Main program
if __name__ == "__main__":
    # Create new Parser object with 2nd command-line arg
    fileName = sys.argv[1]
    asmParser = Parser(fileName)

    # Create 

    
