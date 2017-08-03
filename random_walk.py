#!/usr/bin/python

# What is the longest random walk you can take so that on average you shall end up n blocks or fewer than home

import random
import time
walkable_distance = 5


def random_walk(steps):
    x, y = 0, 0
    for step in range(steps):
        x1, y1 = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        x += x1
        y += y1
    return x, y


def monte_carlo_simulation(runs):
    for walk in range(1, 51):
        count = 0
        t = time.clock()
        for i in range(runs):
            (x, y) = random_walk(walk)
            distance_from_home = abs(x) + abs(y)
            if distance_from_home <= walkable_distance:
                count += 1
        walkable_percentage = round(float(count/runs) * 100, 2)
        elapsed = time.clock() - t
        print("For walk length {} , the walkable percentage is {}. Ran MC simulation for {} runs in {:.2f} seconds.".format(walk, walkable_percentage, runs, elapsed))

print(monte_carlo_simulation(50000))


