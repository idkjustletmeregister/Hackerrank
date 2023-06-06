#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    
    if len(arr) > 4:
        arrs = sorted(arr)
        print(arrs[0]+arrs[1]+arrs[2]+arrs[3], arrs[-4]+arrs[-3]+arrs[-2]+arrs[-1])
    
    else:
        print(sum(arr), sum(arr))
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
