import numpy as np 
print("Enter each row of your first matrix. After you've entered the last row, enter an empty row.")
A = []
while True:
    a = input("Row:") #input Rows
    if not a.strip():
        break #break after user inputs empty row
    A.append(list(map(float, a.split()))) #append rows to list of lists


print("A = ", A)

for x in A:
    col_number_A = (len(x)) 


print("Enter each row of your second matrix. After you've entered the last row, enter an empty row.")
B = []
while True:
    b = input("Row:") #input rows of second matrix
    if not b.strip():
        break #break after user inputs empty row
    B.append(list(map(float, b.split()))) #append rows to list of lists

print("B = ", B)

row_number_B = len(B) 

if col_number_A == row_number_B: #ensure number of columns of matrix A and number of rows of matrix B are the same
    result = np.dot(A, B)
    print(result)
else:
    print("These matrices cannot be multiplied. Make sure the number of columns in Matrix A corresponds to the number of rows in Matrix B!")
