import numpy as np

if __name__ == "__main__":
    n,m,p = map(int,input().split())
    
    a = np.array([input().split() for _ in range(n)],int)
    b = np.array([input().split() for _ in range(m)],int)
    
    print(np.concatenate((a,b),axis =0))
