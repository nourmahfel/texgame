NAME
miRNA-Gene-Disease - This tool provides information on association of different miRNAs to genes to diseases and association of different diseases to genes to miRNAs. 

SYNOPSIS

Optional arguments:
 [-h], [ --help]        Show this help message and exit
 [-sm]                    Look up miRNAs available in the database
 [-sd]                     Look up diseases available in the database
 [--mirna]               Enter the name of miRNA for output of associated diseases and genes
 [--disease]            Enter the name of disease in quotes ("") for output of associated miRNAs and genes
 [--conf] {80-101}   Enter a confidence score to filter results. Choices include a range of integers from 80-101
 [--score] {False}   Enter the command option score False for displaying results without the score

DESCRIPTION

**miRNA-Gene-Disease** This tool provides information on association of different miRNAs to diseases and association of different diseases to miRNAs. Furthermore, the tool provides information on genes associated with different miRNAs and diseases. Note that the tool only provides information on miRNAs and diseases that are available in the database. To look up if a disease/miRNA present in the database use -sd and -sm commands with part of a miRNA/disease. Command input -sd all or -sm all provides information on all available diseases and miRNAs in the database.

EXAMPLES

python database.py --mirna hsa-miR-4299
The command shows output of diseases and genes associated with hsa-miR-4299. Provides information on confidence scores of the results. 
python database.py --sm all
Prints all miRNAs that are available in the database
python database.py --sd neuro
Searches for diseases in the database that contain “neuro” and prints the diseases. 
python database.py –disease "CARDIOMYOPATHY DILATED 1HH" --score False --conf 90
The command shows output of miRNAs and genes associated with CARDIOMYOPATHY DILATED 1HH with confidence score more or equal to 90.
python database.py --disease "Hereditary Coproporphyria"
The command shows output of miRNAs and genes associated with Hereditary Coproporphyria. It also provides information on confidence scores of the results. 

COMPATIBILITY 

Compatible with Python 3

LIBRARIES

Pandas, regex, numpy, sys, argparse, tabulate

AUTHOR

Nour Mahfel
