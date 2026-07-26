# Ask the user to enter a positive integer
n = int(input("Enter a positive integer: "))

# Display the column headings
print("Number\tSquare\tCube")

# Display numbers, their squares, and cubes
for i in range(1, n + 1):
    print(i, "\t", i**2, "\t", i**3)