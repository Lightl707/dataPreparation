import numpy as np

#1 - Matrix Transpose - [1,3][2,4]
m = np.array([[1, 2], [3, 4]])
tr = np.transpose(m)
print(tr)

#2  - Dot Product of scalar values
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
sol = np.dot(m1, m2)
print(sol)

#3 - Mean - 48.5
a = np.array([7,16,23,45,77,123])
mean_a = np.mean(a)
print("Mean a:", mean_a)

#4 - Median - 34.0
a = np.array([7,16,23,45,77,123])
median_a = np.median(a)
print("Median a:", median_a)

#5 - Minimum - 7
a = np.array([7,16,23,45,77,123])
min_a = np.min(a)
print("Minimum a:", min_a)

#6 - Max - 123
a = np.array([7,16,23,45,77,123])
max_a = np.max(a)
print("Maximum a:", max_a)

#7 - Sum of 2 array - [ 3  7 11 15 19 25]
a = np.array([1,3,5,7,9,12])
b = np.array([2,4,6,8,10,13])
ab_sum = np.add(a,b)
print(ab_sum)

#8 - Difference of 2 array - [-1 -1 -1 -1 -1 -1]
a = np.array([1,3,5,7,9,12])
b = np.array([2,4,6,8,10,13])
ab_diff = np.subtract(a,b)
print(ab_diff)

#9 Square root of array - [ 5.  6.  7.  1.  2.  3. 11.]
a = np.array([25,36,49,1,4,9,121])
a_sqrt = np.sqrt(a)
print(a_sqrt)

#10 Reshape array - [[1 5 7][2 3 4]]
a = np.array([1,5,7,2,3,4])
b = np.reshape(a, (2,3))
print(b)

#11 Transposed array - [[1 2][5 3][7 4]]
a = np.array([1,5,7,2,3,4])
b = np.reshape(a, (2,3))
c = np.transpose(b)
print(c)

#12 Standard Deviation - 40.42173507738958
a = np.array([7,16,23,45,77,123])
b = np.std(a)
print(b)

#13 Percentile of NumPy Array - 17.75, 34.0
a = np.array([7,16,23,45,77,123])
b = np.percentile(a, 25)
c = np.percentile(a, 50)
print(b)
print(c)

#14 Solution of a system of linear equations 2x+3y=12,4x−y=5 => x = 27/14, y = 19/7
a = np.array([[2, 3], [4, -1]])
b = np.array([12, 5])
solution = np.linalg.solve(a, b)
print(solution)

#15 Determinant of matrix - 1 * 3 - 2 * 7 = -11
a = np.array([[1, 2], [7, 3]])
d = np.linalg.det(a)
print(d)

