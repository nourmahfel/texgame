import re
import os.path
import sys
import argparse 

def FastaFile (value): #Defining a new function that recognises FastaFile format.
    if os.path.isfile(value)==False:
        raise argparse.ArgumentTypeError("file %s does not exist" % value)
    i_value= value.split(".")
    if i_value[1]!="fasta": #Specifes the types of the file that will be acceptable for reading line by line. 
        raise argparse.ArgumentTypeError("%s does not have a .fasta extension" % value) #Asks for input of the correct file type. 
    return value
parser= argparse.ArgumentParser()# The program defines the arguments required for argparse output. 
parser.add_argument("i", help= "Input the name of the fasta file containing the proteins", type= FastaFile) #Argument parser is used to assist the user to input the file name required for file recognition.
parser.add_argument("enz_digest", help= "Name of the enzyme to digest the proteins", choices= ["trypsin","lys-c", "arg-c", "v8_prot"])# The code only identifies these four enzymes. If any other enzyme name is inputted in the command line, the terminal will error trap it and provide the possible options for enzyme input. 
args=parser.parse_args()

def readFastaFile(file): # Defines a function to input an protein fasta file and outputs the sequences as a string.
    FastaFile = open(file, 'r') #Opens the file.
    sequences = {} # Creates a dictionary to contain all of the sequences. 
    names = [] # Creates a list to contain all of the names.
    for line in FastaFile:
        if line.startswith('>'):  # Identifies headers through the symbol ">".
            header = line[1:].rstrip('\n') # Ignores the header line character ">" and removes new lines.
            name = header.split()[0] #Takes first word in the header. This command splits the line at the first word and returns it to name.
            names.append(name) # Appends the first word to the list. 
            sequences[name] = '' # Assigning name as the key in the dictionary. 
        else:
            sequences[name] += line.rstrip('\n') # If it is not a header line, then a new line is concatinated onto the growing string, which is indexed as "name".
    FastaFile.close() # It will close the file upon finishing reading all of the lines. 
    return (sequences, names) # Returns the sequences and the names. Sequences are put in dictionary and names are put in lists. 

file=args.i
(mySeqs, seqNames) = readFastaFile(file)

def enzyme_digest(): # Defining a new function "enzyme_digest" to input the digested peptides.
    if args.enz_digest =="trypsin": # Conditional statement "if", the user chooses trypsin to digest proteins.
        print('The output is printed in file task2t.peps') # The output is printed into a file. The terminal will output the name of the file based on chosen enzyme.
        file_path = 'task2t.peps' # Specifies the filepath in python.
        sys.stdout = open(file_path, "w") #Opens the file in the same directory. 
        for name in seqNames: #Iterating over the key "names" to access the proteins in the dictionary. 
            seq = mySeqs[name] # Specifies the sequences that are cut by trypsin.
            seq= re.sub(r'([KR])([^P])', r'\1*\2', seq) #Regular expression is used to input "*" after K or R, unless there is a P after it in the protein sequence. 
            peps=seq.split(r'*') #Splits the sequences at "*".Allows trypsin to cut at K and R unless there is a P after it. 
            for i in range(0,len(peps)): # Iterates over a list of peptides.
                print('>',name, end='') # The header is printed after '>'.
                if i==0: # Conditional statement "If", recognises the peptides at position 1.
                    print(' peptide {0:1} N trypsin'.format(i+1)) #Assigns N-terminal to first peptides. The count for number of peptides starts from 1.
                    print(peps[i]) #The digested peptides are printed in the correct format.
                elif i==len(peps)-1: # Conditional statement "else If", recognises the peptides at the last position and assigns C-terminal to the peptides.
                    print(' peptide {0:1} C trypsin'.format(i+1)) 
                    print(peps[i]) # The digested peptides are printed accordingly.
                else: #Conditional statement "else", peptides are internal "I" within the sequence.
                    print(' peptide {0:1} I trypsin'.format(i+1)) #Assigns I-terminal to internal peptides.
                    print(peps[i]) # The digested peptides are printed accordingly.
                    
    elif args.enz_digest == "lys-c": # Conditional statement "if", the user chooses endoproteinase lys-c to digest proteins.
        print('The output is printed in file task2el.peps') # The output is printed into a file. The terminal will output the name of the file based on chosen enzyme.
        file_path = 'task2el.peps' #The file path is specified.
        sys.stdout = open(file_path, "w")
        for name in seqNames: #Iterates over a string of proteins.
            seq = mySeqs[name] 
            seq= re.sub(r'([K])([^P])', r'\1*\2', seq) #Regular expression is used to input "*" after K, unless there is a P after it in the protein sequence.
            peps=seq.split(r'*') # Splits the sequences at "*".Allows lys-c to cut at K, unless there is a P after it. 
            for i in range(0,len(peps)): # As afformentioned, the for loop iterates over a list of peptides. 
                print('>',name, end='')# The header is printed after '>'.
                if i==0:# Conditional statement "If", recognises the peptides at position 1.
                    print(' peptide {0:1} N Endoproteinase Lys-C'.format(i+1))#Assigns N-terminal to first peptides. The count for number of peptides starts from 1.
                    print(peps[i]) # The digested peptides are printed accordingly.
                elif i==len(peps)-1:# Conditional statement "else If", recognises the peptides at the last position in the cut sequence.
                    print(' peptide {0:1} C Endoproteinase Lys-C'.format(i+1)) #Assigns C-terminal to the last peptides.
                    print(peps[i]) #The digested peptides are printed accordingly.
                else: #Conditional statement "else", recognises internal peptides.
                    print(' peptide {0:1} I Endoproteinase Lys-C'.format(i+1)) #Assigns I-terminal to internal peptides.
                    print(peps[i]) #Prints peptides accordingly. 
                    
    elif args.enz_digest == "arg-c": # Conditional statement "if", the user chooses endoproteinase arg-c to digest proteins.
        print('The output is printed in file task2ea.peps') # The output is printed into a file. The terminal will output the name of the file based on chosen enzyme.
        file_path = 'task2ea.peps'#The file path is specified.
        sys.stdout = open(file_path, "w")
        for name in seqNames:
            seq = mySeqs[name]
            seq= re.sub(r'([R])([^P])', r'\1*\2', seq)  #Regular expression is used to input "*" after R, unless there is a P after it in the protein sequence.
            peps=seq.split(r'*') # Splits the sequences at "*".Allows arg-c to cut at R, unless there is a P after it. 
            for i in range(0,len(peps)): # The for loop iterates over a list of peptides. 
                print('>',name, end='') #The header is printed after '>'.
                if i==0:# Conditional statement "If", recognises the peptides at position 1.
                    print(' peptide {0:1} N Endoproteinase Arg-C'.format(i+1))#Assigns N-terminal to first peptides. The count for number of peptides starts from 1.
                    print(peps[i])#Prints peptides accordingly. 
                elif i==len(peps)-1:# Conditional statement "else If", recognises the peptides at the last position in the cut sequence.
                    print(' peptide {0:1} C Endoproteinase Arg-C'.format(i+1))#Assigns C-terminal to the last peptides.
                    print(peps[i]) #Prints peptides accordingly. 
                else: #Conditional statement "else", recognises internal peptides.
                    print(' peptide {0:1} I Endoproteinase Arg-C'.format(i+1))#Assigns I-terminal to internal peptides.
                    print(peps[i])
                    
    elif args.enz_digest == "v8_prot": # # Conditional statement "if", the user chooses v8 proteinase to digest proteins.
        print('The output is printed in file task2v.peps') # The output is printed into a file. The terminal will output the name of the file based on chosen enzyme.
        file_path = 'task2v.peps' #The file path is specified.
        sys.stdout = open(file_path, "w")
        for name in seqNames: #Iterates over a string of proteins.
            seq = mySeqs[name]
            seq= re.sub(r'([E])([^P])', r'\1*\2', seq) #Regular expression is used to input "*" after E, unless there is a P after it in the protein sequence.
            peps=seq.split(r'*') # Splits the sequences at "*".Allows v8_proteinase to cut at E, unless there is a P after it. 
            for i in range(0,len(peps)): # The for loop iterates over a list of peptides.
                print('>',name, end='') #The header is printed after '>'.
                if i==0:# Conditional statement "If", recognises the peptides at position 1.
                    print(' peptide {0:1} N V8 Proteinase'.format(i+1))#Assigns N-terminal to first peptides. The count for number of peptides starts from 1.
                    print(peps[i])#Prints peptides accordingly.
                elif i==len(peps)-1: # Conditional statement "else If", recognises the peptides at the last position in the cut sequence.
                    print(' peptide {0:1} C V8 Proteinase'.format(i+1))#Assigns C-terminal to the last peptides.
                    print(peps[i])#Prints peptides accordingly.
                else: #Conditional statement "else", recognises internal peptides.
                    print(' peptide {0:1} I V8 Proteinase'.format(i+1))#Assigns I-terminal to internal peptides.
                    print(peps[i]) #Prints peptides accordingly.
enzyme_digest()
