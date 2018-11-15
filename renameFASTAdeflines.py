# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:35:07 2016

@author: Lucas Boatwright
"""

from Bio.SeqIO.FastaIO import SimpleFastaParser
from sys import argv, stderr
import argparse
from datetime import datetime

def parse_arguments():
    """Parse arguments passed to script"""
    parser = argparse.ArgumentParser(description=
    "This script is designed to rename the deflines in a FASTA file and \
    \ngenerate a table with old_defline<TAB>new_defline. Resulting FASTA \
    \nputs each entry sequence on one line.\n\n \
    \nUsage: python {0} -f file.fasta -d new_defline \n".format(argv[0]),
    formatter_class = argparse.RawDescriptionHelpFormatter)

    requiredNamed = parser.add_argument_group('required arguments')

    requiredNamed.add_argument("-f", "--FASTA", type=str, required=True,\
    help="Input FASTA file.", action="store")

    parser.add_argument("-d", "--DEFLINE", type=str, required=False,\
    help="The new defline to replace the old. Deflines will be numbered staring \
    \nat one. Default: Transcript \n\n(Ex. -d Transcript --> Transcript_1)", 
    action="store", default="Transcript")

    parser.add_argument("-m","--HASHMAP", type=str, required=False,\
    help="Rename a FASTA file using a pre-existing hashmap \
    \nFormat: old<TAB>new.",
    action="store")

    return parser.parse_args() 


def rename_fasta_from_hashmap(file_name, hashmap):
    """Rename FASTA defline using new base name"""
    hash = {}
    with open(hashmap,'r') as f:
        for line in f:
            split_line = line.split()
            hash[split_line[0]]=split_line[1]
    output_base_name = file_name.split(".fa")[0]
    output_fasta = open(output_base_name + ".renamed.fa", "w")
    with open(file_name) as handle:
        for values in SimpleFastaParser(handle):
            output_fasta.write(">" + hash[values[0].split()[0]] + "\n")
            output_fasta.write(values[1] + "\n")
    output_fasta.close()


def rename_fasta_and_log_output(file_name, base_name="Transcript"):
    """Rename FASTA defline using new base name"""
    output_base_name = file_name.split(".fa")[0]
    output_fasta = open(output_base_name + ".renamed.fa", "w")
    output_table = open(output_base_name + ".renamed.table","w")
    base_name_counter = 1
    with open(file_name) as handle:
        for values in SimpleFastaParser(handle):
            output_fasta.write(">" + base_name + "_" + 
                str(base_name_counter) + "\n")
            output_fasta.write(values[1] + "\n")
            output_table.write(values[0].split()[0] + "\t" + base_name + "_" + 
                str(base_name_counter) + "\n")
            base_name_counter += 1
    output_fasta.close()


if __name__ == "__main__":
    start = datetime.now()
    args = parse_arguments()
    stderr.write("Executed: python {0} -f {1} -d {2}\n".format(argv[0],
                 args.FASTA,args.DEFLINE))    
    
    stderr.write("Re-naming FASTA file.\n")
    if args.HASHMAP:
        rename_fasta_from_hashmap(args.FASTA, args.HASHMAP)
    else:
        rename_fasta_and_log_output(args.FASTA, args.DEFLINE)
