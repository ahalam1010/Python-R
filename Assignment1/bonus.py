# Lab 3 - Bonus Challenge Problems

# Bonus 1: Find the second largest element in a list
numbers = [12, 45, 7, 89, 34, 89, 56]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

unique_numbers.sort(reverse=True)

print("Bonus 1: Second largest element")
print("List:", numbers)
print("Second largest element:", unique_numbers[1])
print()


# Bonus 2: Rotate a list one position to the right
numbers = [1, 2, 3, 4, 5]

rotated_list = [numbers[-1]] + numbers[:-1]

print("Bonus 2: Rotate list one position to the right")
print("Original list:", numbers)
print("Rotated list:", rotated_list)
print()


# Bonus 3: Merge two sorted lists into a single sorted list
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

merged_list = []
i = 0
j = 0

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged_list.append(list1[i])
        i += 1
    else:
        merged_list.append(list2[j])
        j += 1

while i < len(list1):
    merged_list.append(list1[i])
    i += 1

while j < len(list2):
    merged_list.append(list2[j])
    j += 1

print("Bonus 3: Merge two sorted lists")
print("First sorted list:", list1)
print("Second sorted list:", list2)
print("Merged sorted list:", merged_list)
print()


# Bonus 4: Create a multiplication table using nested lists
multiplication_table = []

for i in range(1, 11):
    row = []
    for j in range(1, 11):
        row.append(i * j)
    multiplication_table.append(row)

print("Bonus 4: Multiplication table using nested lists")

for row in multiplication_table:
    print(row)

print()


# Bonus 5: Generate all prime numbers between 1 and 100 using list comprehension
prime_numbers = [
    number
    for number in range(2, 101)
    if all(number % divisor != 0 for divisor in range(2, number))
]

print("Bonus 5: Prime numbers between 1 and 100")
print(prime_numbers)