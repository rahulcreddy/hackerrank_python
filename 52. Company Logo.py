#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    
    chars = Counter(sorted(s))
    
    for i in chars.most_common(3):
        print(*i)
