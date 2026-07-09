# Remove all duplicate elements from a list.

numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("Original list:", numbers)
print("List after removing duplicates:", unique_numbers)