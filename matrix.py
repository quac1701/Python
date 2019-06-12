import numpy
import math

A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
res = 0
for m in range(2**9):
	for x in range(3):
		for y in range(3):
			A[x][y] = m >> (x * 3 + y) & 1
	if abs(numpy.linalg.det(A) - 0) > 1e-9:
		res += 1
print(res)
