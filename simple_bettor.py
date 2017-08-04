#!/usr/bin/python

import random


def roll_dice():
    roll = random.randint(1, 100)

    if roll == 100 or roll <= 50:  # 51% chance of failure
        return False
    else:
        return True


def simple_bettor(count, funds=10_000, wager=100):
    amount = funds
    wager_count = 0
    while wager_count < count and amount > 0:
        if roll_dice():
            amount += wager
        else:
            amount -= wager
        wager_count += 1
    return amount


# Lets start betting for 1 to n rounds and find the percentage of wins (earning > initial_investment) in increments
# of {interval}. Even with only 1% odd against you, we see no# of bets is inversely proportional to percentage of wins.
# Moral: As you gamble more odds are stacked against you.

interval = 100
initial_amount = 10_000
for start in range(1, 20001, interval):
    win_count = 0
    for x in range(start, start + interval):
        amount = 0
        amount = simple_bettor(x)
        if amount > initial_amount:
            win_count += 1
            # print('Won with ${} in {} rounds'.format(amount, x))
        else:
            win_count = win_count
            # print('Lost with ${} in {} rounds'.format(amount, x))

        # Calculate percentage of wins in last {interval} rounds
        if x % interval == 0:
            print('{}% wins in last 100 rounds starting {} and ending {}'.format(round(float(win_count/interval) * 100, 2), x - (interval - 1), x))
