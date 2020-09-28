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


def find_combinations(integer: int) -> list:
    """
    Find all permutations of length x (integer)

    Based on a given integer, identify all possible combinations that can be
    made based on the numbers between 1 and the integer. Calling the function
    with 3 as integer, this results in a total of six different combinations:
    3 * 2 * 1 = 6. Each combination of numbers is reported as list of lists

    :param integer: int, maximum length of each combination
    :return: list, all permutations that are possible
    """

    length = 1

    # create a separate list for each unique element
    permutations = [[number] for number in range(1, integer + 1)]
    while length < integer:
        temp_list = []
        for perm in permutations:
            for i in range(1, integer + 1):
                temp_list.append(perm + [i])
        permutations = temp_list
        length += 1

    return permutations


def generate_kmer_combinations(combinations: list) -> dict:

    bases = ['a', 't', 'c', 'g']
    kmer_collection = {}
    for combination in combinations:
        temp_sequence = []
        for integer in combination:
            temp_sequence.append(bases[integer - 1])
        kmer_collection[''.join(temp_sequence)] = 0

    return kmer_collection


def kmer_occurrence(kmers: list, kmer_combinations: dict) -> dict:
    """
    Count the occurrence of each kmer in a string

    :param kmers: list, a collection of k-mers
    :param kmer_combinations: dict, all possible combinations of kmers
    :return: dict, the occurrence of each k-mer in the string
    """

    for kmer in kmers:
        if kmer in kmer_combinations:
            kmer_combinations[kmer] += 1
    return kmer_combinations


def report_occurrence(kmer_occurrence: dict):
    """
    Report the occurrence of each k-mer in lexicographical order

    :param kmer_occurrence: dict, the occurrence of each k-mer
    """

    sorted_kmers = {kmer: count for kmer, count in sorted(kmer_occurrence.items(), key=lambda item: item[0])}
    with open("answer_file.txt", 'w') as writer:
        writer.write(' '.join(str(count) for count in list(sorted_kmers.values())))


if __name__ == "__main__":
    dna_seq = argv[1]
    fasta_dict = parse_fasta(dna_seq)
    fasta_string = list(fasta_dict.values())[0]
    kmer_list = create_kmers(fasta_string, 4)
    integer_combinations = find_combinations(4)
    kmer_counts = kmer_occurrence(kmer_list, generate_kmer_combinations(integer_combinations))
    report_occurrence(kmer_counts)
