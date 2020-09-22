"""
Compute the GC content and report the sequence with the highest content

Author: Dominique Massau
"""

# imports
from sys import argv


# functions
def parse_fasta(file_name: str) -> dict:
    """
    Parse a fasta file into a dictionary

    :param file_name: str, name of the fasta file
    :return: dict, contains fasta header: DNA sequence
    """

    with open(file_name, 'r') as lines:
        fasta_dict = {}
        for line in lines:
            if line.startswith('>'):
                current_header = line.strip('>').strip()
                fasta_dict[current_header] = []
            else:
                fasta_dict[current_header].append(line.strip().lower())

    for header, seq in fasta_dict.items():
        fasta_dict[header] = ''.join(seq)
    return fasta_dict


def calculate_gc_content(fasta_dict: dict) -> list:
    """
    Calculate the GC percentage for every fasta sequence

    :param fasta_dict:
    :return: list, contains tuple with fasta header: GC perc
    """

    gc_perc_list = []
    for header, seq in fasta_dict.items():
        gc_perc_list.append((header, (seq.count('c') + seq.count('g'))
                             / len(seq)))
    return gc_perc_list


if __name__ == "__main__":
    fasta_seqs = parse_fasta(argv[1])
    gc_perc_list = calculate_gc_content(fasta_seqs)
