#!/usr/bin/python

# Problem 14
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers
# finish at 1.
#
# Which starting number, under one million, produces the longest chain?

import time

dictionary = {}


def collatz(n):
    if n in dictionary:
        return dictionary.get(n), n
    else:
        if n == 1:
            dictionary[n] = 1
        elif n % 2 == 0:
            dictionary[n] = collatz(int(n / 2))[0] + 1
        else:
            dictionary[n] = collatz(int(3 * n + 1))[0] + 1
        return dictionary.get(n), n


start = time.time()
print(max(tuple(collatz(i) for i in range(500_000, 1_000_000))))
elapsed = (time.time() - start)
print("Time: {:.5f} seconds".format(elapsed))
