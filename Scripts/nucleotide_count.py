"""
Script to count the number of nucleotides in a single DNA string.

Author: Dominique Massau
Date: 21/09/2020
"""

# imports
from sys import argv


# functions
def parse_string(text_file) -> str:

    with open(text_file) as dna_strings:
        for dna_str in dna_strings:
            yield dna_str


if __name__ == "__main__":
    print(parse_string(argv[1]))
