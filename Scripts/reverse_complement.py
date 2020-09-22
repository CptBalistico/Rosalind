"""
Script to produce the reverse complement of a DNA sequence

Author: Dominique Massau
Date: 22/09/2020
"""

# imports
from dna_to_rna import write_output
from nucleotide_count import parse_dna_string
from sys import argv


# functions
def get_reverse_complement(dna_str: str) -> str:
    """

    :param dna_str: str, a DNA sequence
    :return: str, reverse complement of the DNA sequence
    """

    complement_dna = []
    for nucleotide in dna_str:
        if nucleotide == 'a':
            complement_dna.append('t')
        elif nucleotide == 't':
            complement_dna.append('a')
        elif nucleotide == 'c':
            complement_dna.append('g')
        else:
            complement_dna.append('c')
    return ''.join(complement_dna).upper()[::-1]


if __name__ == "__main__":
    dna_string = parse_dna_string(argv[1])
    complement = get_reverse_complement(dna_string)
    write_output(complement, "complementary_dna.txt")

