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

# Importing modules
import sys  # lets us access the command-line arguments (just the .asm file in our case)
from SymbolTable import SymbolTable
from Parser import Parser


# Extra function that compares hack files line by line
def compareHacks(given, produced):
    # Open files
    givenFile = open(given)
    producedFile = open(produced)

    # First get number of lines in each file and check if theyre the same
    count1 = 0
    count2 = 0
    for line in givenFile:
        count1 += 1
    for line in producedFile:
        count2 += 1
    if count1 != count2:
        print("File contents dont match!")
        givenFile.close()
        producedFile.close()
        return
    
    # Compare content line by line
    for i in range(count1):
        originalLine = givenFile.readline()
        newLine = producedFile.readline()
        if originalLine != newLine:
            print("File contents dont match!")
            givenFile.close()
            producedFile.close()
            return

    # If we got here, success
    print("YAY! File contents match!!")
    givenFile.close()
    producedFile.close()


# Main program (THE ASSEMBLER!)
if __name__ == "__main__":
    fileName = sys.argv[1]

    # First Pass: Read all commands, only paying attention to labels and updating the symbol table
    try:
        ourFile = open(fileName, 'r')
    except IOError:
        print("Could not open file", fileName)
        sys.exit()
    
    with ourFile:
        n = 0
        updatedSymbolTable = SymbolTable()
        label = ourFile.readline()
        # While not at the end of the file
        while label != '':
            # If the command is not a comment or all whitespace
            if not label.isspace():
                # Strip white space before first character occurrence
                label = label.lstrip()
                # If the command is not a comment
                if not label[0:2] == "//":
                    
                    # If "(" starts the command, its a label to be added
                    if label[0] == "(":
                        # First, strip any comment or whitespace away
                        label = label.strip()
                        if "//" in label:
                            endPos = label.find("//")
                            label = label[0 : endPos]
                        # Add the label and its value (n) to the table
                        label = label[1 : len(label)-1]
                        updatedSymbolTable.addEntry(label, n)

                    # Else, its an a or c instruction, so just increment n
                    else:
                        n += 1

            # Read next line
            label = ourFile.readline()

    print("Added labels to symbol table!")

    # Second pass: restart reading and translating commands, write to MyProg.hack
    with open("MyProg.hack", 'w') as newHackFile:
        asmParser = Parser(fileName, updatedSymbolTable)
        bits = asmParser.advance()
        while bits != '':
            # If advance() returned something other than 0, write to hack file (and new line)
            if bits:
                newHackFile.write(bits)
                newHackFile.write("\n")
            # Next line
            bits = asmParser.advance()
    
    print("Wrote codes to MyProg.hack!")

    # Comparing the hack files (commented because for my own use, feel free to uncomment and check)
    #fileNameHack = fileName[0 : len(fileName)-4] + ".hack"
    #compareHacks(fileNameHack, "MyProg.hack")