# Take a 3 x 3 matrix from the user and calculate row sums, column sums, and total sum.

matrix = []

print("Enter values for a 3 x 3 matrix:")

for i in range(3):
    row = []
    for j in range(3):
        value = int(input("Enter value: "))
        row.append(value)
    matrix.append(row)

print("Matrix:")

for row in matrix:
    print(row)

total_sum = 0

print("Row sums:")

for row in matrix:
    row_sum = 0
    for value in row:
        row_sum += value
        total_sum += value
    print(row_sum)

print("Column sums:")

for column in range(3):
    column_sum = 0
    for row in range(3):
        column_sum += matrix[row][column]
    print(column_sum)

print("Total sum:", total_sum)