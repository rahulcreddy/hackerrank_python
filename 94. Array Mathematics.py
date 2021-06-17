import numpy as np

if __name__ == "__main__":
    n,m = map(int,input().split())
    
    a = np.array([input().split() for _ in range(n)], int)
    b = np.array([input().split() for _ in range(n)], int)
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)
    print(a**b)
