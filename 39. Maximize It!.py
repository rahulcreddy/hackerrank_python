# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product


if __name__ == "__main__":
    k,m = map(int,input().split(" "))
    
    n = [list(map(int,input().split(" ")))[1:] for _ in range(k)] #exclude the length
    
    all_sum = map(lambda arr: sum(x*x for x in arr)%m,product(*n))
    print(max(all_sum))
