#!/usr/bin/python

# Problem 13
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
import time

start = time.time()
print(sum(int(n.strip()) for n in tuple(open('test3.txt', 'r'))))
elapsed = time.time() - start
print("Time: {:.5f} seconds".format(elapsed))