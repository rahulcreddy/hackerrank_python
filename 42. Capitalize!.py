#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    check = 1
    new = ""
    for i in range(len(s)):
        if(s[i] == " "):
            new += s[i]
            check = 1
        else:
            if(check == 1):
                new += s[i].upper()
                check = 0
            else:
                new += s[i]
    return new


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
