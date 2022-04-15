import numpy as np
A1 = (input("Enter the first row of your first 3x3 matrix:"))
a1 = list(A1)
a1 = [ele for ele in a1 if ele.strip()]
a1 = list(map(int, a1))

A2 = (input("Enter the second row of your first 3x3 matrix:"))
a2 = list(A2)
a2 = [ele for ele in a2 if ele.strip()]
a2 = list(map(int, a2))

A3 = (input("Enter the third row of your first 3x3 matrix:"))
a3 = list(A3)
a3 = [ele for ele in a3 if ele.strip()]
a3 = list(map(int, a3))

A = []
A.append(a1)
A.append(a2)
A.append(a3)


B1 = (input("Enter the first row of your second 3x3 matrix:"))
b1 = list(B1)
b1 = [ele for ele in b1 if ele.strip()]
b1 = list(map(int, b1))

B2 = (input("Enter the second row of your second 3x3 matrix:"))
b2 = list(B2)
b2 = [ele for ele in b2 if ele.strip()]
b2 = list(map(int, b2))

B3 = (input("Enter the third row of your second 3x3 matrix:"))
b3 = list(B3)
b3 = [ele for ele in b3 if ele.strip()]
b3 = list(map(int, b3))

B = []
B.append(b1)
B.append(b2)
B.append(b3)

result = np.dot(A, B)
print(result)


