import numpy

n = int(input())
mat = numpy.array([input().split() for _ in range(n)],float)

print(round(numpy.linalg.det(mat),2))
