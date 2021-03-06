
# FASTA scripts

This repository contains scripts for dealing with FASTA files and identifies external scripts as well

## randomFasta

built from [FastaUtils](https://github.com/jlboat/FastaUtils)

```
usage: java -jar randomFasta.jar -n <#Seqs> -l <LenSeqs>
 -h,--help           Print this help message
 -l,--length <arg>   Length of sequences (default: 200)
 -n,--number <arg>   Number of sequences (default: 200)
 -o,--output <arg>   Output file name (required)
```

## fastaStats

built from [FastaUtils](https://github.com/jlboat/FastaUtils)

```
usage: java -jar fastaStats-1.0.jar -i <input> -o <output>
 -h,--help           Print this help message
 -i,--input <arg>    Input FASTA file
 -o,--output <arg>   Output file name (default: stdout)
```

## generateFASTAhistogram

```
usage: generateFASTAhistogram.py [-h] --file FILE --hist HIST [--bins BINS]

This script was designed to generate histograms for FASTA sequence lengths.

optional arguments:
  -h, --help   show this help message and exit
  --file FILE  Input file. Output from fastaStats.jar
  --hist HIST  Choose which type of histogram to generate. --hist d (density)
               --hist f (frequency).
  --bins BINS  Optionally choose bin count for the frequency histogram
```

## renameFASTAdeflines.py

```
usage: renameFASTAdeflines.py [-h] -f FASTA [-d DEFLINE] [-m HASHMAP]

This script is designed to rename the deflines in a FASTA file and     
generate a table with old_defline<TAB>new_defline. Resulting FASTA     
puts each entry sequence on one line.

     
Usage: python renameFASTAdeflines.py -f file.fasta -d new_defline 

optional arguments:
  -h, --help            show this help message and exit
  -d DEFLINE, --DEFLINE DEFLINE
                        The new defline to replace the old. Deflines will be
                        numbered staring at one. Default: Transcript (Ex. -d
                        Transcript --> Transcript_1)
  -m HASHMAP, --HASHMAP HASHMAP
                        Rename a FASTA file using a pre-existing hashmap
                        Format: old<TAB>new.

required arguments:
  -f FASTA, --FASTA FASTA
                        Input FASTA file.
```

## Extract sequences from FASTA

See Picard:

```
java -jar picard.jar ExtractSequences \
      INTERVAL_LIST=regions_of_interest.interval_list \
      R=reference.fasta \
      O=extracted_IL_sequences.fasta
```
