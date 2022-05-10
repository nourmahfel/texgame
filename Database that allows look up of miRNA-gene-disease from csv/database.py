import argparse
import sys
import regex
import pandas
import numpy # Import libraries to run the script


df=pandas.read_csv('./miRNA-Gene-Disease.csv', header = 0, sep=',' ) #Read the dataset miRNA-Gene-Disease
parser= argparse.ArgumentParser()# The program defines the arguments required for argparse output.

parser = argparse.ArgumentParser(prog = 'miRNA-Gene-Disease',
                                 usage = '''
                                 [-sd Look up diseases available in the database. Input a part of miRNA name for search. Command option [-sd all] prints all diseases in the database]
                                 [-sm Look up miRNAs available in the database. Input a part of disease name for search. Command option [-sm all] prints all miRNAs in the database]
                                 [--mirna Provide miRNA name for output of gene and disease association]
                                 [--disease Provide the Disease name in quotes ("") for output of diasease and gene association]
                                 [--score Enter the command option False for displaying results without the score]
                                 [--conf Enter a confidence score to filter results above the given confidence score ]
                                 ''',
                                 description = '''
                                 Description:
                                 This tool provides information on association of different miRNAs to diseases and association of different diseases to miRNAs.
                                 Furthermore, the tool provides information on genes associated with different miRNAs and diseases.
                                 Note that the tool only provides information on miRNAs and diseases that are available in the database.
                                 To look up if a disease/miRNA present in the database use -sd and -sm commands with part of a miRNA/disease.
                                 ''',
                                 add_help = True
                                 ) #Description of the tool and how to use it. 
                                   #One argument is required for each command, if no argument is provided, argparse will print the usage and description.
                                   #If an empty argument is provided argparse will error trap it and will print the number of arguments required
parser.add_argument("-sm", type = str, help = "Look up miRNAs available in the database")
parser.add_argument("-sd", type = str, help = "Look up diseases available in the database") #Argument parser is used to assist the user to input the appropriate commands. 
parser.add_argument("--mirna", type = str, help = "Enter the name of miRNA for output of associated diseases and genes", action = 'store') 
parser.add_argument("--disease", type= str, help = "Enter the name of disease for output of associated miRNAs and genes")
parser.add_argument("--conf", type= int, help = "Enter a confidence score to filter results, default is set at 80", choices = range(80,101))
parser.add_argument("--score", type = str, help = "Enter the command option score False for displaying results without the score", choices= ['False'])
args=parser.parse_args()

df1_filtered = df[df["Score-g-d"] >= args.conf] #Optional argument if a user chooses to filter miRNA or disease based on a confidence score
df2_filtered = df[df["Score-m-g"] >= args.conf]

if args.sd:   #Different outputs are printed based on the arguments chosen.
    sd = df.Disease[df['Disease'].str.contains(args.sd, flags=regex.IGNORECASE)]
    if args.sd == "all":
        print(df[['Disease']].drop_duplicates().to_markdown(index=False))
    elif sd.shape[0]== 0: #Error handling, if a user inputs name or part of disease that is not present in the database.
        print("Disease is not in database. Please use the command option [-sm all] for a list of diseases present in the database")
    else:
        print(sd.drop_duplicates().to_markdown(index=False))
elif args.sm:
    sm = df.miRNA[df['miRNA'].str.contains(args.sm, flags=regex.IGNORECASE)]
    if args.sm == "all": #If a user chooses to look through all miRNAs available in the database
        print(df[['miRNA']].drop_duplicates().to_markdown(index=False))
    elif sm.shape[0]== 0: #Error handling, if a user inputs a name or part of miRNA that is not present in the database.
        print("miRNA is not in database. Please use the command option [-sm all] for a list of miRNAs present in the database")
    else:
        print(sm.drop_duplicates().to_markdown(index=False))

elif args.disease and args.conf: #The user chooses a confidence score for the output.
    disease= df1_filtered.loc[df['Disease'] == args.disease, ['miRNA','Gene','Score-g-d']]
    d_score = df1_filtered.loc[df['Disease'] == args.disease, ['miRNA','Gene']]
    if disease.shape[0]== 0: #Error handling, if a user inputs a name of disease that is not present in the database.
        print("Disease with the confidence score provided is not in database")
    elif args.score: #If the user chooses not to present the scores in the output.
        print(d_score.drop_duplicates().to_markdown(tablefmt="grid", index = False))
    else:
        print(disease.drop_duplicates().to_markdown(tablefmt="grid", index = False))
elif args.disease and not args.conf: #If the user does not choose a confidence score for the output.
    disease= df.loc[df['Disease'] == args.disease, ['miRNA','Gene','Score-g-d']]
    d_score = df.loc[df['Disease'] == args.disease, ['miRNA','Gene']]
    if disease.shape[0]== 0:
        print("Disease is not in database")
    elif args.score: #If the user chooses not to present the scores in the output.
        print(d_score.drop_duplicates().to_markdown(tablefmt="grid", index = False))
    else:
        print(disease.drop_duplicates().to_markdown(tablefmt="grid", index = False))

elif args.mirna and args.conf: #The user chooses a confidence score for miRNA-Gene.
    mir = df2_filtered.loc[df['miRNA'] == args.mirna, ['Gene','Disease', 'Score-m-g']]
    mir_score = df2_filtered.loc[df['miRNA'] == args.mirna, ['Disease','Gene']]
    if mir.shape[0]== 0:
        print("miRNA with the confidence score provided is not in database")
    elif args.score:
        print(mir_score.to_markdown(tablefmt="grid", index = False))
    else:
        print(mir.to_markdown(tablefmt="grid", index = False))
elif args.mirna and not args.conf:
    mir = df.loc[df['miRNA'] == args.mirna, ['Gene','Disease', 'Score-m-g']]
    mir_score = df.loc[df['miRNA'] == args.mirna, ['Disease','Gene']]
    if mir.shape[0]== 0:
        print("miRNA is not in database")
    elif args.score:
        print(mir_score.drop_duplicates().to_markdown(tablefmt="grid", index = False))
    else:
        print(mir.drop_duplicates().to_markdown(tablefmt="grid", index = False))
else: #If no commands are presented the help message will appear.
    parser.print_help(sys.stderr)
    print()
    print("Provide an optional command or commands for miRNA-Gene-Disease association using the commands available above")
    sys.exit(1)
#Switch method implementation method only available in java 
