"""
Script to determine the k-mer composition of a DNA sequence

Author: Dominique Massau
Date: 28/09/2020
"""

# imports
from gc_content import parse_fasta
from sys import argv


# functions


if __name__ == "__main__":
    fasta_dict = parse_fasta(argv[1])