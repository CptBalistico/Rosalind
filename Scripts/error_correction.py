"""
Correct an erogenous nucleotide in a reads

Author: Dominique Massau
Date: 27/09/2020
"""

# imports
from gc_content import parse_fasta
from reverse_complement import get_reverse_complement
from sys import argv


# functions
def check_pairs(fastas: dict):
    """
    Check whether at least two pairs are present

    :param fastas: dict, contains header: sequence
    :return:
    """

    pairs = {}

    for seq in fastas.values():
        reverse_comp = get_reverse_complement(seq).lower()
        if seq in pairs:
            pairs[seq].append(seq)
        elif reverse_comp in pairs:
            pairs[reverse_comp].append(seq)
        else:
            pairs[seq] = []

    # Separately store reads that occur only once
    error_reads = [seq_1 for seq_1, seq_2 in pairs.items() if seq_2 == []]

    return error_reads, fastas.values()


if __name__ == "__main__":
    fasta_dict = parse_fasta(argv[1])
    check_pairs(fasta_dict)