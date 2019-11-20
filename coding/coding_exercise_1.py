#Original function as sent by jampp.

import random

def weighted_random(values, weights):
    total_weight = sum(weights)
    acum_weights = [w / total_weight for w in weights[:]]
    for i in range(len(weights)):
        acum_weights[i] += acum_weights[i]
        rand = random.random()
    for value, weight in zip(values, acum_weights):
        if weight > rand:
            return value
