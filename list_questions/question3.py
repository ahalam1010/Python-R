num = [-5, -2, -1, 0, 1, 2, 3]

sum = 0
for i in num:
    sum += i

average = sum / len(num)

max = num[0]

for i in num:
    if i > max:
        max = i

min = num[0]

for i in num:
    if i < min:
        min = i
    
print(f"The sum: {sum}")
print(f"The average: {average}")
print(f"The maximum: {max}")
print(f"The minimum: {min}")

