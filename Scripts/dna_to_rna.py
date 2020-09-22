"""
Script to convert a DNA string to an RNA string

Author: Dominique Massau
Date: 22/09/2020
"""

# imports
from nucleotide_count import parse_dna_string
from sys import argv


def convert_dna_to_rna(dna_str: str) -> str:
    """
    Convert a DNA sequence into an RNA sequence

    :param dna_str: str, sequence of a DNA sequence
    :return: str, sequence of a corresponding RNA segment
    """

    nucleotide_list = ['u' if nucleotide == 't' else nucleotide
                       for nucleotide in dna_str]
    return ''.join(nucleotide_list).upper()


if __name__ == "__main__":
    dna_string = parse_dna_string(argv[1])
    rna_string = convert_dna_to_rna(dna_string)
    print(rna_string)
