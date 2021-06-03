import numpy as np

if __name__ == "__main__":
    p = list(map(float,input().split()))
    x = float(input())
    
    print(np.polyval(p,x))
