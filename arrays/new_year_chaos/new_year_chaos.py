#!/bin/python3

import math
import os
import random
import re
import sys

from functools import reduce


def minimumBribes(q):
    # Write your code here
    changes = 0
    # iterate through the input array
    for i in range(len(q)):
        higher = 0
        # if the current element
        # moved of more than 2 positions then print Too chaotic 
        # and return
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        try:
            # if the element X has shifet to the right, count the 
            # number of elements higher than X. 
            higher = reduce(lambda x, y: x + y, map(
                lambda x: 1 if x > q[i] else 0, q[max(0, q[i]-2):i]))
        except TypeError as e:
            # empty list passed to reduce 
            pass
        changes += higher
    print(changes)
    

    
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

