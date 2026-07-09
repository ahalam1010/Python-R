# Reverse a list using reverse() and list slicing.

numbers = [1, 2, 3, 4, 5]

reverse_method = numbers.copy()
reverse_method.reverse()

slicing_method = numbers[::-1]

print("Original list:", numbers)
print("Reversed using reverse():", reverse_method)
print("Reversed using slicing:", slicing_method)