"""
Script to count the number of nucleotides in a single DNA string.

Author: Dominique Massau
Date: 21/09/2020
"""

# imports
import re
from sys import argv


# functions
def parse_dna_string(text_file: str) -> str:
    """
    Parse a DNA string from a text file

    :param text_file: str, name for file with a DNA string
    :return: str, contains letters A, C, G and T only
    """

    with open(text_file) as dna_strings:
        for dna_str in dna_strings:
            if is_valid_sequence(dna_str.strip()):
                return dna_str.strip().lower()
            else:
                raise ValueError("Invalid char in sequence")


def count_nucleotides(dna_str: str) -> dict:
    """
    Count the number of A, C, G and T nucleotides of a string

    :param dna_str: str, sequence of a DNA segment
    :return: dict, contains the nucleotide: count
    """

    nucleotide_dict = {}
    for nucleotide in dna_str:
        if nucleotide not in nucleotide_dict:
            nucleotide_dict[nucleotide] = 1
        else:
            nucleotide_dict[nucleotide] += 1
    return nucleotide_dict


def is_valid_sequence(dna_str: str) -> bool:
    """
    Checks if the DNA segment only contains valid chars (A, C, G, T)

    :param dna_str: str, sequence of a DNA segment
    :return: bool, True if the DNA sequence is valid
    """

    # pattern only matches to DNA nucleotides A, C, G and T
    pattern = re.compile(r'^[*ACGT]+$', re.IGNORECASE)
    if re.match(pattern, dna_str):
        return True
    else:
        return False


if __name__ == "__main__":
    dna_string = parse_dna_string(argv[1])
    nucleotide_count = count_nucleotides(dna_string)

