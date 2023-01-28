#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    i = 0
    # optimise at each step 
    # greedy
    while i < len(arr):
        # if the current element is not in it's position
        # swap to the correct position
        if arr[i]-1 != i:
            _tmp0, _tmp1  = arr[i], arr[arr[i]-1]
            arr[_tmp0-1] = arr[i]
            arr[i] = _tmp1
            swaps += 1
        else:
            i += 1 
    return swaps
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

