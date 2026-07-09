numbers = [1, 2, 2, 3, 1, 1]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print("List:", numbers)

for number in frequency:
    print(number, "->", frequency[number])