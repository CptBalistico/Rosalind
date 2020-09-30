"""
Script to translate an RNA sequence to a protein

Author: Dominique Massau
Date: 29/09/2020
"""

# imports
from codons import amino_acids
from nucleotide_count import parse_string
from sys import argv


# functions
def rna_to_protein(rna_string: str) -> str:
    """
    Convert an RNA sequence into an amino acid sequence

    :param rna_string: str, RNA sequence
    :return: str, amino acid sequence
    """

    aa_list = []
    position = 0

    while position + 4 < len(rna_string):
        codon = rna_string[position:position + 3].upper()

        if codon == '_':
            break

        aa_list.append(amino_acids[codon])
        position += 3

    return ''.join(aa_list)


def report_protein(aa_sequence: str):
    """
    Write the amino acid sequence to a file

    :param aa_sequence: str, amino acid sequence
    """

    with open("answer_file.txt", 'w') as writer:
        writer.write(aa_sequence)


if __name__ == "__main__":
    rna_str = parse_string(argv[1])
    report_protein(rna_to_protein(rna_str))
