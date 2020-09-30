"""
Script to excise intronic sequences from DNA and translate it to a protein

Author: Dominique Massau
Date: 29/09/2020
"""

# imports
from dna_to_rna import convert_dna_to_rna
from gc_content import parse_fasta
from translate_rna import rna_to_protein
from translate_rna import report_protein
from sys import argv


# functions
def extract_headers(text_file: str) -> list:
    """
    Extract all headers from a text file with fasta sequences

    :param text_file: str, name of the file with fasta sequences
    :return: list, all headers corresponding to the fasta sequences
    """

    headers = []
    with open(text_file, 'r') as lines:
        for line in lines:
            if line.startswith('>'):
                headers.append(line.strip('>').strip())
    return headers


def excise_introns(sequence: str, introns: list) -> str:
    """
    Excise intronic subs sequences from the main DNA sequence

    :param sequence: str,  main sequence
    :param introns: list, to be excised intronic sequences
    :return: str, DNA sequences without intronic sequences
    """

    intron_cords = []
    for intron in introns:
        for i in range(len(sequence)):
            if intron == sequence[i:i + len(intron)]:
                intron_cords.append((i, i + len(intron)))

    intron_cords = sorted(intron_cords)

    exons = []
    for pos, cords in enumerate(intron_cords):
        if pos == 0:
            exons.append(sequence[:cords[0]])
        else:
            exons.append(sequence[intron_cords[pos - 1][1]:cords[0]])
    exons.append(sequence[intron_cords[-1][1]:])
    return ''.join(exons)


if __name__ == "__main__":
    fasta_list = extract_headers(argv[1])
    fasta_seqs = parse_fasta(argv[1])
    main_seq = fasta_seqs[fasta_list[0]]
    substrings = [fasta_seqs[header] for header in fasta_list[1:]]

    excised_sequence = excise_introns(main_seq, substrings)
    rna_seq = convert_dna_to_rna(excised_sequence.lower())
    report_protein(rna_to_protein(rna_seq))
