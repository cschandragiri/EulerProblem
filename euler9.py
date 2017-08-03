#!/usr/bin/python

# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time

start = time.time()

for num in range(1, 1000):
    for dig in range(num, 1000 - num):
        i = 1000 - num - dig
        if num * num + dig * dig == i * i:
            print(num, dig, i)
            print("Product: {}".format(num * dig * i))

elapsed = time.time() - start
print("Time: {:.5f} seconds".format(elapsed))

