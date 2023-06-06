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
    
    pos, neg, zer = 0, 0, 0
    
    for num in arr:
        if num < 0:
            neg += 1
        elif num > 0:
            pos += 1
        else:
            zer += 1
    
    print("%.6f\n%.6f\n%.6f" % (pos/n, neg/n, zer/n))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr,n)
