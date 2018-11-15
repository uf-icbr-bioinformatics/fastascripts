# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 13:42:56 2016

@author: Lucas Boatwright
"""

from pandas import DataFrame
import argparse
import sys

def parse_arguments():
    """Parse arguments passed to script"""
    parser = argparse.ArgumentParser(description="This script was " + 
            "designed to generate histograms for FASTA sequence lengths.\n\n")

    parser.add_argument("--file", type=str, required=True, \
    help="Input file. Output from fastaStats.jar \n",
    action="store")

    parser.add_argument("--hist", type=str, required=True, \
    help="Choose which type of histogram to generate. \n" +
    "\n--hist d (density) " + 
    "\n--hist f (frequency).\n\n", 
    action="store")
        
    parser.add_argument("--bins", type=str, required=False, \
    help="Optionally choose bin count for the frequency histogram", 
    action="store")

    return parser.parse_args()

    
def interactive_lengths_histogram(lengths, mean, n50, bins):
    """Generate histogram of contig lengths"""
    import matplotlib.pyplot as plt
    bins = int(bins)
    if bins:
        n, bins, patches = plt.hist(lengths, bins=bins, facecolor='g')
    else:
        n, bins, patches = plt.hist(lengths, facecolor='g')
    mean_ax = plt.axvline(mean, color="blue")
    n50_ax = plt.axvline(n50, color="red")
    plt.xlabel('Lengths (bp)')
    plt.ylabel('Frequency')
    plt.legend([mean_ax, n50_ax],["Mean","N50"])
    plt.grid(False)
    plt.show()


def seaborn_histograms(lengths, mean, n50):
    """Use seaborn to generate nicer histograms"""
    import matplotlib.pyplot as plt
    import seaborn as sns    
    sns.set(style="white", palette="muted")
    sns.distplot(lengths, hist=False, color="g", 
                 kde_kws={"shade": True})
    mean_ax = plt.axvline(mean, color="blue")
    n50_ax = plt.axvline(n50, color="red")
    plt.xlabel("Lengths (bp)")
    plt.ylabel("Density")
    plt.legend([mean_ax, n50_ax],["Mean","N50"])
    plt.tight_layout()
    plt.show()
    

def main(args):
    """Execute functions according to input"""
    lengths = []
    mean = 0
    n50 = 0
    with open(args.file) as f:
        for line in f:
            if ">" in line:
                lengths.append(int(line.split()[1]))
            elif "Mean:" in line:
                mean = float(line.split()[1])
            elif "N50:" in line:
                n50 = float(line.split()[1])

    if ((mean==0) or (n50==0) or (len(lengths)==0)):
        sys.stderr.write("\nNo sequences found in stats file.\n\n")
        sys.exit(-1)
    if args.hist == "f":
        if args.bins:
            interactive_lengths_histogram(lengths, mean, n50, args.bins)
        else:
            bins = 0
            interactive_lengths_histogram(lengths, mean, n50, bins)
    elif args.hist == "d":
        seaborn_histograms(lengths, mean, n50)
    else:
        sys.stderr.write("\nInvalid histogram option.\n\n")
        sys.exit(-1)


if __name__ == "__main__":
    args = parse_arguments()
    main(args)

