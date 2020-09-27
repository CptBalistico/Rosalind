"""
Script to create a superstring using substrings

Author: Dominique Massau
Date: 26/09/2020
"""

# imports
from gc_content import parse_fasta
from overlap_graphs import is_similar_sequence
from sys import argv


# functions
def find_overlap(fastas: dict) -> str:
    """
    Assemble fasta sequences with overlapping ends

    :param fastas: dict, contains header: NDA sequence
    :return: string, assembled sequence
    """

    sequences = list(fastas.values())

    while len(sequences) > 1:
        for query_seq in sequences:
            hit_found = False
            for target_seq in sequences:

                if is_similar_sequence(query_seq, target_seq):
                    continue

                alignment = align_sequences(query_seq, target_seq)
                if alignment[0]:
                    sequences.remove(query_seq)
                    sequences.remove(target_seq)
                    sequences.insert(0, alignment[1])
                    hit_found = True
                    break

            if hit_found:
                break

    return sequences[0]


def align_sequences(query_seq: str, target_seq: str) -> tuple:
    """
    Try to align a sequence against another sequence

    The query and target represent a DNA sequence. Expanding substrings
    of the target are compared against the query in stepwise fashion. When
    an overlap of at least 10 characters is found, a hit is returned.
    In case the entire query has been covered and no hit has been found,
    the alignment is stopped.

    :param query_seq: str, DNA sequence of the query
    :param target_seq: str, DNA sequence of the target to be aligned
    :return: tuple, bool (found a hit or not) and if so, the aligned sequence
    """

    main_pos = len(query_seq)   # position of the alignment between query and target
    position = 0    # length of the substring of the query and target

    while main_pos >= 0:
        if query_seq[main_pos:(main_pos + len(target_seq))] == target_seq[:position] and position >= 10:
            return True, query_seq + target_seq[position:]
        position += 1   # increase size of the substrings each iteration by 1
        main_pos -= 1   # decrease the position of the query each iteration by 1

    return False, None


if __name__ == "__main__":
    fasta_dict = parse_fasta(argv[1])
    assembly = find_overlap(fasta_dict)

    with open('answer_file', 'w') as writer:
        writer.write(assembly.upper())
