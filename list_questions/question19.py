marks = [81, 82, 83, 84, 85, 86, 87, 88, 89, 90]

sum = 0

highest = max(marks)
lowest = min(marks)

print("The highest mark: ", highest)
print("The lowest mark: ", lowest)

for i in marks:
    sum += i

average = sum / len(marks)

print("The average: ", average)

above_average = 0

for i in marks:
    if i > average:
        above_average += 1

print("Students above average: ", above_average)
        