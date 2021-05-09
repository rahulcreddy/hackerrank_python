# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement as cr

if __name__ == "__main__":
    s,k = input().split(" ")
    k = int(k)
    s = sorted(s)
    
    print(*["".join(i) for i in cr(s,k)], sep = "\n")
