import numpy as np

n,m = map(int,input().split())

a = np.array([input().split() for _ in range(n)], int)

print(np.mean(a, axis = 1), np.var(a, axis = 0), np.round(np.std(a),11), sep = "\n")
