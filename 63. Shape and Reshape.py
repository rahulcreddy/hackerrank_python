import numpy as np

if __name__ == "__main__":
    arr = np.array(list(map(int, input().split())))
    arr.shape = (3,3)
    print(arr)
