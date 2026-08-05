matrix = []

for i in range(3):
    rows = list(map(int, input("Enter 3 numbers: ").split()))
    matrix.append(rows)

# Calculating the rows

for row in matrix:
    row_sum = 0

    for num in row:
        row_sum += num
    print("Rows Sum: ", row_sum) 

# Calculating the cols 

for col in range(3):
    col_sum = 0

    for row in range(3):
        col_sum += matrix[row][col]
    print("Columns Sum: ", col_sum)

# Calculating the total

total = 0

for row in matrix:
    for num in row:
        total += num

print("The total: ", total) 

