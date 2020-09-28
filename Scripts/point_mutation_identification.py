"""
Identify point mutations and report the hamming distance

Author: Dominique Massau
Date: 27/09/2020
"""

# imports
from nucleotide_count import is_valid_sequence
from sys import argv


# functions
def parse_dna_seq(text_file: str) -> list:
    """
    Parse one or more DNA sequences in a list

    :param text_file: str, name of the file with DNA sequences
    :return: list, contains DNA sequences
    """
    sequences = []
    with open(text_file, 'r') as lines:
        for line in lines:
            sequences.append(line.strip())
    return sequences


def identify_mutations(sequences: list) -> int:
    """
    Identify the count of point mutations between two sequences
    :param sequences: list, contains two sequences (strings)
    :return: int, the hamming distance between the two sequences
    """

    hamming_distance = 0
    for char_1, char_2 in zip(sequences[0], sequences[1]):
        if char_1 != char_2:
            hamming_distance += 1
    return hamming_distance


if __name__ == "__main__":
    dna_sequences = parse_dna_seq(argv[1])
    for sequence in dna_sequences:
        if not is_valid_sequence(sequence):
            raise ValueError("Invalid characters in sequence")
    print(identify_mutations(dna_sequences))
