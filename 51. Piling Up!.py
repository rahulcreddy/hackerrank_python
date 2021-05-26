# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

n = int(input())

for _ in range(n): 
    deq_size = int(input())
    deq = deque(map(int,input().split()))
    
    for i in reversed(sorted(deq)):
        if deq[0] == i:
            deq.popleft()
        elif deq[-1] == i:
            deq.pop()
        else:
            print("No")
            break
    else:
        print("Yes")
