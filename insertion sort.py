#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(len(arr)):
        key=arr[i]
        count=0
        while key<arr[i-1-count] and i-1-count>=0:
            arr[i-count]=arr[i-1-count]
            for k in arr:
                print(k,end=' ')
            arr[i-1-count]=key
            count=count+1
            print()
    for z in arr:
        print(z,end=' ')
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
