#Solution for the exercise.
#This function gives a weighted random value from a list.

from itertools import accumulate
import random

def weighted_random(values, weights):
    total_weight = sum(weights)
    norm_weights = [w / total_weight for w in weights[:]]
    acum_weights = list(accumulate(norm_weights))
    rand = random.random()
    for value, weight in zip(values, acum_weights):
        if weight > rand:
            return value
