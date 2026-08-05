num = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

even = []
odd = []

for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f"The number of even elements: {even}")
print(f"The number of odd elements: {odd}")

print(len(even))
print(len(odd))