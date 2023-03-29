#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    
    sp = ' '
    ch = '#'
    
    for j in range(1,n+1):
        print(f'{sp*(n-j)}{ch*j}')


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
