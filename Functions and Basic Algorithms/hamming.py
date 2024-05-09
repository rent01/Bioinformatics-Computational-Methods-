# -*- coding: utf-8 -*-
# @Author : TY Ren
# @Email : ren.tiany@northeastern.edu
# @Software : PyCharm
# @Time : 1/25/2023 7:21 PM
# @File : hamming.py
# -------------------------------
import sys

# test input
dna1 = 'ACCATA'
dna2 = 'CATTGA'


def hamming(dna1, dna2):
    """
    find the hamming disntance between two DNA strings
    """
    if len(dna1) == len(dna2):
        i = 0
        d = 0
        while i < len(dna1):
            if dna1[i] != dna2[i]:
                i += 1
                d += 1
            else:
                i += 1
        return (d)
    else:
        raise ValueError("Error!! The length of the string has to be same")


if __name__ == "__main__":
    dna1 = sys.argv[1]
    dna2 = sys.argv[2]
    distance = hamming(dna1, dna2)
    # use tabs to separate DNA strings
    print("The 1st DNA string is:", dna1 + "\t" + "The 2nd DNA string is:", dna2 + "\t" +
          "the hamming distance is: {}".format(str(distance)))

