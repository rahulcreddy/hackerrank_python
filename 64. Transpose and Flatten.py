import numpy as np

if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = np.array([input().split() for _ in range(n)],int)
    print(np.transpose(arr))
    print(arr.flatten())
