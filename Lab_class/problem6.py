rows = int(input("Enter the number of rows: "))

total_values = 0

for row in range(1, rows + 1):
    for number in range(1, row + 1):
        print(number, end=" ")
        total_values += 1

    print()

print("Total number of values printed:", total_values)