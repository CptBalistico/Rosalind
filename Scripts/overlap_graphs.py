"""
Script to find nodes that are adjacent to each other

Author: Dominique Massau
Date: 25/09/2020
"""

# imports
from sys import argv
from gc_content import parse_fasta


# functions
def find_overlap(fasta_dict: dict) -> list:
    """
    Find overlap between two sequences

    :param fasta_dict: dict, contains header: sequence
    :return: list, contains headers of sequences with overlap of 3
    """

    overlap_headers = []
    for query_header, query_sequence in fasta_dict.items():
        for target_header, target_sequence in fasta_dict.items():
            if is_similar_sequence(query_sequence, target_sequence):
                continue
            else:
                if target_sequence[-3:] == query_sequence[0:3]:
                    overlap_headers.append([target_header, query_header])
    return overlap_headers


def is_similar_sequence(seq_1: str, seq_2:str) -> bool:
    """
    Check if two sequences are identical

    :param seq_1: str, sequence
    :param seq_2: str, sequence
    :return: bool, 1 if sequences are equal and false otherwise
    """

    if seq_1 == seq_2:
        return True
    else:
        return False


if __name__ == "__main__":
    fasta_dict = parse_fasta(argv[1])
    for header_hit in find_overlap(fasta_dict):
        print(' '.join(header_hit))
