# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

words = OrderedDict()

n = int(input())

for _ in range(n):
    item = input()
    if words.get(item):
        words[item] += 1
    else:
        words[item] = 1
        
print(len(words))
print(*words.values())
