#!/usr/bin/python

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

s = filter(lambda n: n % 2 == 0, map(lambda n: n * n, nums))
print(list(s))
