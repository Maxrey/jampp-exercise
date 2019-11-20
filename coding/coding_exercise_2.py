#Original function as given by jampp.

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

"""
Testing the function "as is".
A "coin flip" test is done for values= [0,1], for different sets of weights.
Obtaining a sample set of values for n iterations of the function allows to get an approximation of the weights
(with less error as n goes higher).

"""
#Giving input variables for the function

values = [0,1]
weights = [0.25, 0.75]

#Creating a sample set

iterations=0
sample_set = []

while iterations<1000:
    sample_set.append(weighted_random(values,weights))
    iterations+=1

# Recalculating the weights from our sample set:

zeros_count= sample_set.count(0)
ones_count= sample_set.count(1)
sample_zeros_weight= zeros_count / iterations
sample_ones_weight= ones_count / iterations
print (sample_set)
print (sample_zeros_weight)
print (sample_ones_weight)

"""
Evaluating for both weights = 0.5 gives a list full of zeroes.
Evaluating for a high enough number of iterations a couple of times, the set weights seem to oscillate around some random weight, not the ones from the input:
    - for input weights [0.4, 0.6], values around  [0.2, 0.8] are obtained.
    - for input weights [0.3, 0.7], values around  [0.4, 0.6] are obtained.
    - for input weights [0.25, 0.75], values around  [0.5, 0.5] are obtained.

Conclusion:
The function is clearly wrong, however from this i can't tell yet why.
"""
