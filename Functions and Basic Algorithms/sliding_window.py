# -*- coding: utf-8 -*-
# @Author : TY Ren
# @Email : ren.tiany@northeastern.edu
# @Software : PyCharm
# @Time : 1/25/2023 6:15 PM
# @File : sliding_window.py
# -------------------------------
import sys


def sliding_window(k, string):
    """
    the first step is to find a k-mer size
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
    string = sys.argv[2]

    kmers = sliding_window(k, string)
    for i in range(len(kmers)):
        # Print the result, rounding GC content to 2 decimal places
        print("{}\t{:.2f}".format(kmers[i], gc_content(kmers[i])))
