numbers = [12, 5, 8, 20, 3, 15]

total = 0
maximum = numbers[0]
minimum = numbers[0]

for number in numbers:
    total += number

    if number > maximum:
        maximum = number

    if number < minimum:
        minimum = number

average = total / len(numbers)

print("List:", numbers)
print("Sum:", total)
print("Average:", average)
print("Maximum value:", maximum)
print("Minimum value:", minimum)