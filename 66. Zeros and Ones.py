import numpy as np

if __name__ == "__main__":
    l = list(map(int, input().split()))
    print(np.zeros(l, dtype = np.int))
    print(np.ones(l, dtype = np.int))
