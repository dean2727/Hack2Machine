'''
File: SymbolTable.py
Author: Dean Orenstein
Date: 04/07/2020
Section: 511
E-mail: dean27@tamu.edu

Description:
SymbolTable class: manages the symbol table (Hack assembly language symbols)
'''

class SymbolTable:
    # Constructor: creates new symbol table (with the predefined symbols) and mnemonic tables
    def __init__(self):
        self.symbolTable = {
            'R0':0, 'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5, 'R6':6, 'R7':7, 'R8':8,
            'R9':9, 'R10':10, 'R11':11, 'R12':12, 'R13':13, 'R14':14, 'R15':15,
            "SCREEN":16384, "KBD":24576, 
            "SP":0, "LCL":1, "ARG":2, "THIS":3, "THAT":4
        }
        self.compTable = {
            "0":"0101010", "1":"0111111", "-1":"0111010", "D":"0001100", "A":"0110000", 
            "M":"1110000", "!D":"0001101", "!A":"0110001", "!M":"1110001", "-D":"0001111", 
            "-A":"0110011", "-M":"1110011", "D+1":"0011111", "A+1":"0110111", "M+1":"1110111", 
            "D-1":"0001110", "A-1":"0110010", "M-1":"1110010", "D+A":"0000010", "D+M":"1000010", 
            "D-A":"0010011", "D-M":"1010011", "A-D":"0000111", "M-D":"1000111", "D&A":"0000000", 
            "D&M":"1000000", "D|A":"0010101", "D|M":"1010101"
        }
        self.destTable = { "M":"001", "D":"010", "MD":"011", "A":"100", "AM":"101", "AD":"110", "AMD":"111" }
        self.jumpTable = { "JGT":"001", "JEQ":"010", "JGE":"011", "JLT":"100", "JNE":"101", "JLE":"110", "JMP":"111" }
    
    # Adds a symbol-address (key-value) pairing to the table
    def addEntry(self, symbol, address):
        self.symbolTable[symbol] = address

    # Returns true if the table already contains the symbol
    def contains(self, symbol):
        if symbol in self.symbolTable:
            return True
        else:
            return False

    # Return the address (integer) associated with the symbol
    def getAddress(self, symbol):
        return self.symbolTable[symbol]