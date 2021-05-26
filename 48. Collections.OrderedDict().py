# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

n = int(input())

orders = OrderedDict()

for _ in range(n):
    item, space, price = input().rpartition(' ')
    
    if orders.get(item):
        orders[item] += int(price)
    else:
        orders[item] = int(price)
        
for item,price in orders.items():
    print(item, price)
