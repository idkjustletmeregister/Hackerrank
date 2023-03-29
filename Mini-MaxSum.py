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
    
    mini, maxi = 0, 0
    arr = sorted(arr)
    
    if len(arr) >= 4:  
        for i in range(0,4):
            mini += arr[i]
            maxi += arr[len(arr)-i-1]
            
        print(mini, maxi)
            
    else:
        print(sum(arr), sum(arr))
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
