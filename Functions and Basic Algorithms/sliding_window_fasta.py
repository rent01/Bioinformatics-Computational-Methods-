# -*- coding: utf-8 -*-
# @Author : TY Ren
# @Email : ren.tiany@northeastern.edu
# @Software : PyCharm
# @Time : 1/25/2023 10:42 PM
# @File : sliding_window_fasta.py
# -------------------------------
import re
import sys


def sliding_window(k, string):
    """
    we need to revise this code, that takes k-mers and fasta, not a string
    """
    kmers = []
    end = len(string) - k + 1
    for start in range(0, end):
        kmers.append(string[start:start + k])

    return kmers

def gc_content(dna):
    """
    the second step is to find GC content
    """
    # For consistency, make the sequence lowercase
    dna = dna.lower()

    # Count the number of g's and c's
    gc = 0
    for nucleotide in dna:
        if nucleotide in ['g', 'c']:
            gc += 1
    return gc / len(dna)

if __name__ == "__main__":
    """Check to make sure there are at least two arguments"""
    arg_count = len(sys.argv) - 1
    if arg_count < 2:
        raise Exception("This script requires 2 arguments: a kmer size and then a string")

    k = int(sys.argv[1])
    # we need to change string into fasta file
    fasta = sys.argv[2]

    in_sequence = False
    current_header = ""
    current_sequence = ""

    with open(fasta, 'r') as f:
        for line in f:
            # If the line starts with '>', it's a header
            if line.startswith(">"):
                if in_sequence:
                    kmers = sliding_window(k, current_sequence)
                    for i in range(len(kmers)):
                        print("{}\t{}\t{:.2f}".format(current_header, kmers[i], gc_content(kmers[i])))
                current_header = line.strip()
                current_sequence = ""
                in_sequence = True
            else:
                current_sequence += line.strip()

    kmers = sliding_window(k, current_sequence)
    for i in range(len(kmers)):
        # Print the result, rounding GC content to 2 decimal places
        print("{}\t{:.2f}".format(kmers[i], gc_content(kmers[i])))