# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    pat = input()
    res = True
    
    try:
        reg = re.compile(pat)
    except re.error:
        res = False
    print(res)
