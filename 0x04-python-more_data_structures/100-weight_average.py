#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple (<score>, <weight>)."""
    if not my_list:
        return 0

    weighted_sum = 0
    sum_weights = 0

    for item in my_list:
        weighted_sum += item[0] * item[1]
        sum_weights += item[1]

    return (weighted_sum/sum_weights)
