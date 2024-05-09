# -*- coding: utf-8 -*-
# @Author : TY Ren
# @Email : ren.tiany@northeastern.edu
# @Software : PyCharm
# @Time : 1/25/2023 9:45 PM
# @File : fibonacci.py
# -------------------------------
import sys

def population(n, k):
    """
    we need to find out the population of worms
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    pop = [0] * (n + 1)
    pop[1] = 1
    for i in range(2, n + 1):
        pop[i] = (pop[i - 1] + pop[i - 2] * k)
    return pop[n]

if __name__ == "__main__":
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    print(f"Population at day {n} with rate {k} is: ", population(n, k))
