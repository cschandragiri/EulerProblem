#!/usr/bin/python
# Problem 16
#
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?

import time

start = time.time()
print(sum(map(int, str(2 ** 1000))))
elapsed = (time.time() - start)
print("Time: {:.5f} seconds".format(elapsed))
