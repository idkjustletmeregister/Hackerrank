#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr,n):
    
    pos, zer, neg = 0, 0, 0
    
    for i in range(0,n):
        if arr[i] == 0:
            zer += 1
        elif arr[i] < 0:
            neg += 1
        elif arr[i] > 0:
            pos += 1
    
    print(float("{:.6f}".format( pos/n )))
    print(float("{:.6f}".format( neg/n )))
    print(float("{:.6f}".format( zer/n )))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr,n)