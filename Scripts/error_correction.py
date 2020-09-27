"""
Correct an erogenous nucleotide in a reads

Author: Dominique Massau
Date: 27/09/2020
"""

# imports
from gc_content import parse_fasta
from reverse_complement import get_reverse_complement
from sys import argv


# functions


if __name__ == "__main__":
    fasta_dict = parse_fasta(argv[1])