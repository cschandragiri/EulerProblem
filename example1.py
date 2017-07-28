#!/usr/bin/python

import itertools
import math
import time


#
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        elif number % 2 == 0:
            return False
        else:
            for n in range(3, int(math.sqrt(number) + 1), 2):
                if number % n == 0:
                    return False
            else:
                return True
    return False


def get_primes_sum_gen(limit):
    for number in itertools.count(2):
        if number > limit:
            break
        elif is_prime(number):
            yield number
        number += 1


t1 = time.clock()
print(sum(get_primes_sum_gen(2_000_000)))
t2 = time.clock()
print('Took {} Seconds'.format(t2 - t1))
