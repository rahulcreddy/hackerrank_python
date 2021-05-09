# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations as cb

if __name__ == "__main__":
    n = int(input())
    l = input().split(" ")
    k = int(input())
    
    c = list(cb(l,k))
    num = filter(lambda x: 'a' in x, c)
    print("{0:.3}".format(len(list(num))/len(c)))
