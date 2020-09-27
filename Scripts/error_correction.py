"""
Correct an erogenous nucleotide in a reads

Author: Dominique Massau
Date: 27/09/2020
"""

# imports
from gc_content import parse_fasta
from overlap_graphs import is_similar_sequence
from point_mutation_identification import identify_mutations
from reverse_complement import get_reverse_complement
from sys import argv


# functions
def check_pairs(fastas: dict) -> tuple:
    """
    Check whether at least two pairs are present

    :param fastas: dict, contains header: sequence
    :return: tuple, contains two lists: (1) error reads and (2) all reads
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

    correct_reads = [seq_1 for seq_1, seq_2 in pairs.items() if len(seq_2) > 0]
    error_reads = [seq_1 for seq_1, seq_2 in pairs.items() if seq_2 == []]

    return error_reads, correct_reads


def find_mate(error_reads: list, reads: list) -> dict:
    """
    Determine hamming distance for reads that can be mates

    The reads with an error are compared to all other reads as well as their
    reverse complements. For the pairs, the hamming distance is calculated
    and saved into a dictionary.

    :param error_reads: list, contains reads with an error
    :param reads: list, contains all reads
    :return: dict, contains error reads and other reads with hamming distance
    """

    scores = {error_read: {} for error_read in error_reads}
    for error_read in error_reads:
        for read in reads:

            if is_similar_sequence(error_read, read):
                continue
            else:
                reverse_complement = get_reverse_complement(read).lower()
                norm_hamming_dist = identify_mutations([error_read, read])
                revc_hamming_dist = identify_mutations([error_read, reverse_complement])

                scores[error_read].update({read: norm_hamming_dist})
                scores[error_read].update({reverse_complement: revc_hamming_dist})

    return scores


def report_fixes(scores: dict) -> None:
    """
    Writes a file with fixed reads

    :param scores: dict, contains dict with alternatives and hamming distance
    """

    writer = open("answer_file", 'w')

    for (error_read, fixed_reads) in scores.items():

        best_seen = False
        for k, v in fixed_reads.items():
            if v == 1:
                writer.write(f'{error_read.upper()}->{k.upper()}\n')
                best_seen = True

        if not best_seen:
            raise ValueError("A read contains multiple mistakes")


if __name__ == "__main__":
    fasta_dict = parse_fasta(argv[1])
    error_read_list, read_list = check_pairs(fasta_dict)
    score_dict = find_mate(error_read_list, read_list)
    report_fixes(score_dict)
