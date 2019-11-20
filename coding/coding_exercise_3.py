"""
What I tried now is to look deeper into the function to see how it works, and what is wrong.
Here is the function again.
"""
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
This normalizes the sum of the given weights to 1, obtaining a new list acum_weights=[0.1, 0.8, 0.1].
That sounds normal.
"""

weights = [100,800,100]
total_weight = sum(weights)
acum_weights = [w / total_weight for w in weights[:]]
print(total_weight)
print(acum_weights)

"""
There is something odd in the first for clause.
I modified the function only including the first for clause to see what it does to acum_weights, for the weight values I already have.
"""
def weighted_random_test(weights):
    total_weight = sum(weights)
    acum_weights = [w / total_weight for w in weights[:]]
    for i in range(len(weights)):
        print(i)          # I want to see each item
        acum_weights[i] += acum_weights[i]
        print(acum_weights) # And what it does to the list in each step.

weighted_random_test(weights) #testing the function

"""
I obtain:

0
[0.2, 0.8, 0.1]
1
[0.2, 1.6, 0.1]
2
[0.2, 1.6, 0.2]

The clause sums "i"  to each "i" weight , effectively obtaining 2i for each one.
So, acum_weights= [0.1, 0.8, 0.1] turns into acum_weights=[0.2, 1.6, 0.2]
Whatever happens next in the second for clause, the relation between the weights is already lost. So this is probably what is causing the problem.

"""
