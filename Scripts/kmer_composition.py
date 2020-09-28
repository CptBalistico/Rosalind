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


def kmer_occurence(sequence: str, kmers: list) -> dict:
    """
    Count the occurence of each kmer in a string

    :param sequence: str, a DNA sequence
    :param kmers: list, a collection of k-mers
    :return: dict, the occurrence of each k-mer in the string
    """


def report_occurence(kmer_occurence: dict):
    """
    Report the occurrence of each k-mer in lexicographical order

    :param kmer_occurence:
    """


if __name__ == "__main__":
    fasta_dict = parse_fasta(argv[1])