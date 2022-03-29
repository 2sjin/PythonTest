import numpy as np

x = np.array( [['a', 'b', 'c', 'd'],
               ['c', 'c', 'g', 'h']])

mat_a = np.array( [[10, 20, 30], [10, 20, 30]])
mat_b = np.array( [[2, 2, 2], [1, 2, 3]])

xc = x[x == 'c']
print(xc)
print("'c'의 개수:", xc.size)

print("\nmat_a\n", mat_a)
print("\nmat_b\n", mat_b)

print("\nmat_a - mat_b\n", mat_a - mat_b)

print()