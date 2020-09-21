"""
Script to count the number of nucleotides in a single DNA string.

Author: Dominique Massau
Date: 21/09/2020
"""

# imports
from sys import argv


# functions
def parse_string(text_file) -> str:
    """
    Parse a single string from a text file

    :param text_file: str, name for file containing a string
    :return: dna_str, a sting of any size
    """

    with open(text_file) as dna_strings:
        for dna_str in dna_strings:
            yield dna_str


def count_nucleotides(dna_str) -> dict:
    """
    Count the number of A, C, G and T nucleotides of a string

    :param dna_str: str, represents a DNA segment
    :return: dict, contains the nucleotide: count
    """

    nucleotide_count = {}
    for nucleotide in dna_str:
        if nucleotide not in nucleotide_count:
            nucleotide_count[nucleotide] = 1
        else:
            nucleotide_count[nucleotide] += 1
    return nucleotide_count


if __name__ == "__main__":
    print(parse_string(argv[1]))
