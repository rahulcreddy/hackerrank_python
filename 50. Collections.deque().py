# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

n = int(input())
d = deque()
for _ in range(n):
    command = input().split()
    
    if len(command) > 1:
        eval("d."+command[0]+"("+command[1]+")")
    else:
        eval("d."+command[0]+"()")
                
print(*[item for item in d])
