"""
The problem has something to do with acum_weights.
acum_weights sounds like the intended result is "accumulative weights", and clearly we're not getting that.
I found a function from a library (itertools.accumulate) for getting a list with accumulative weights
so i tried that in the function replacing the broken part of code.
"""
from itertools import accumulate

import random
def weighted_random_modified(values, weights): # renamed to "weighted_random_modified"
    total_weight = sum(weights)
    norm_weights = [w / total_weight for w in weights[:]] # renamed to "norm_weights"
    acum_weights = list(accumulate(norm_weights))
    rand = random.random()
    for value, weight in zip(values, acum_weights):
        if weight > rand:
            return value

"""
I tested the modified the function to see the result with the same "coin flip" used when testing the original function.
"""

values = [0,1]
weights = [0.4,0.6]
iterations=0
sample_set = []

while iterations<10000:
    sample_set.append(weighted_random_modified(values,weights))
    iterations+=1

# Recalculating the weights from our sample set:
zeros_count= sample_set.count(0)
ones_count= sample_set.count(1)
sample_zeros_weight= zeros_count / iterations
sample_ones_weight= ones_count / iterations

print(f'Testing for 2 variables, with values = {values} and weights = {weights}: ')

print (f'For {values[0]}, the set weight is {sample_zeros_weight}')
print (f'For {values[1]}, the set weight is {sample_ones_weight}')

"""
It works!
Now evaluating for both weights = 0.5 gives a sample set consisting of ones and zeros (instead of only zeros as before).
When evaluating different pairs of weights for a high enough number of iterations a couple of times their resultant set weights do indeed tend to the input weights.

Now i want to test the function broadly, including more than two parameters, and draw final conclusions.

"""
values = [1,5,8,4]
weights = [0.2,0.3,0.1,0.4]
iterations=0
sample_set = []

while iterations<100000:
    sample_set.append(weighted_random_modified(values,weights))
    iterations+=1

print(f'Testing for {len(values)} variables, with values = {values} and weights = {weights}: ')

for value in values:
    value_count = sample_set.count(value)
    sample_value_weight= value_count / iterations
    print (f'For {value}, the set weight is {sample_value_weight}')
"""
Works perfectly.
In the case parameters are repeated, the set weight for that repeated parameter tends to the value of the sum of each of the parameters
"""

values = [1,1,8,4,5]
weights = [0.2,0.3,0.1,0.2,0.2]
iterations=0
sample_set = []

while iterations<100000:
    sample_set.append(weighted_random_modified(values,weights))
    iterations+=1

print(f'Testing for {len(values)} variables, with values = {values} and weights = {weights}: ')

for value in values:
    value_count = sample_set.count(value)
    sample_value_weight= value_count / iterations
    print (f'For {value}, the set weight is {sample_value_weight}')
