# Demonstrate append(), insert(), remove(), pop(), clear(), and copy().

numbers = [10, 20, 30]

print("Original list:", numbers)

numbers.append(40)
print("After append(40):", numbers)

numbers.insert(1, 15)
print("After insert(1, 15):", numbers)

numbers.remove(20)
print("After remove(20):", numbers)

removed_item = numbers.pop()
print("After pop():", numbers)
print("Popped item:", removed_item)

copied_numbers = numbers.copy()
print("Copied list:", copied_numbers)

numbers.clear()
print("After clear():", numbers)