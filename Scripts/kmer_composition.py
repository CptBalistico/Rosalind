"""
Script to determine the k-mer composition of a DNA sequence

Author: Dominique Massau
Date: 28/09/2020
"""

# imports
from gc_content import parse_fasta
from sys import argv


# functions
def create_kmers(sequence: str, kmer_size: int) -> list:
    """
    Create a list with k-mers of a specified size from a DNA sequence

    :param sequence: str, a DNA sequence
    :param kmer_size: int, the k-mer size
    :return: list, contains k-mers
    """

    kmers = []
    for position in range(len(sequence)):
        if position + kmer_size <= len(sequence):
            kmers.append(sequence[position:position + kmer_size])
    return kmers


def kmer_occurence(sequence: str, kmers: list) -> dict:
    """
    Count the occurence of each kmer in a string

    :param sequence: str, a DNA sequence
    :param kmers: list, a collection of k-mers
    :return: dict, the occurrence of each k-mer in the string
    """


def report_occurrence(kmer_occurence: dict):
    """
    Report the occurrence of each k-mer in lexicographical order

    :param kmer_occurence: dict, the occurrence of each k-mer
    """


if __name__ == "__main__":
    fasta_dict = parse_fasta(argv[1])
    fasta_string = list(fasta_dict.values())[0]
    create_kmers(fasta_string, 4)