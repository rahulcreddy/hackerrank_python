# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == "__main__":
    s,k = input().split(" ")
    k = int(k)
    s = sorted(s)
    
    for i in range(1,k+1):
        print(*["".join(i) for i in combinations(s,i)], sep = "\n")
