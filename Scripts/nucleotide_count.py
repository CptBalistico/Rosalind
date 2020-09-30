"""
Script to count the number of nucleotides in a single DNA string.

Author: Dominique Massau
Date: 21/09/2020
"""

# imports
import re
from sys import argv


# functions
def parse_string(text_file: str) -> str:
    """
    Parse a DNA string from a text file

    :param text_file: str, name for file with a DNA string
    :return: str, contains letters A, C, G and T only
    """

    with open(text_file) as dna_strings:
        for dna_str in dna_strings:
            if is_valid_sequence(dna_str.strip()):
                return dna_str.strip().lower()


def count_nucleotides(dna_str: str) -> dict:
    """
    Count the number of A, C, G and T nucleotides of a string

    :param dna_str: str, sequence of a DNA segment
    :return: dict, contains the nucleotide: count
    """

    nucleotide_dict = {'a': 0, 'c': 0, 'g': 0, 't': 0}
    for nucleotide in dna_str:
        nucleotide_dict[nucleotide] += 1
    return nucleotide_dict


def report_nucleotide_count(nucleotide_count: dict):
    """
    Reports the count of nucleotides from a dictionary
    :param nucleotide_count: dict, contains count of each nucleotide
    """

    print(f"{nucleotide_count['a']} {nucleotide_count['c']} "
          f"{nucleotide_count['g']} {nucleotide_count['t']}")


def is_valid_sequence(dna_str: str) -> bool:
    """
    Checks if the DNA segment only contains valid chars (A, C, G, T)

    :param dna_str: str, sequence of a DNA segment
    :return: bool, True if the DNA sequence is valid
    """

    # pattern only matches to DNA nucleotides A, C, G and T
    pattern = re.compile(r'^[*ACGTUacgtu]+$', re.IGNORECASE)
    if re.match(pattern, dna_str):
        return True
    else:
        return False


if __name__ == "__main__":
    dna_string = parse_string(argv[1])
    nucl_count = count_nucleotides(dna_string)
    report_nucleotide_count(nucl_count)
