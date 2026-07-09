numbers = [10, 15, 22, 33, 40, 51, 68]

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("List:", numbers)
print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)