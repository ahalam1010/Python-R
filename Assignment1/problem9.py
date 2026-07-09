# Combine two lists using append(), extend(), and + operator.

A = [1, 2, 3]
B = [4, 5, 6]

# Using append()
append_result = A.copy()
append_result.append(B)

# Using extend()
extend_result = A.copy()
extend_result.extend(B)

# Using + operator
plus_result = A + B

print("List A:", A)
print("List B:", B)

print("Using append():", append_result)
print("Using extend():", extend_result)
print("Using + operator:", plus_result)