# Create a 3 x 3 matrix using a nested list.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for row in matrix:
    for value in row:
        total += value

print("Entire matrix:")

for row in matrix:
    print(row)

print("First row:", matrix[0])
print("Last column:", [matrix[0][2], matrix[1][2], matrix[2][2]])
print("Sum of all elements:", total)