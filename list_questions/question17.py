matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Entire matrix: ", matrix)
print("First row: ", matrix[0])

for row in matrix:
    print("Last column: ", row[-1])

total = 0

for row in matrix:
    for num in row:
        total += num

print("The sum: ", total)