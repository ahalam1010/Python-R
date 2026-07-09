# Student marks analysis.

marks = [85, 72, 90, 65, 78, 88, 92, 55, 69, 80]

highest = marks[0]
lowest = marks[0]
total = 0

for mark in marks:
    total += mark

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

average = total / len(marks)

above_average_count = 0

for mark in marks:
    if mark > average:
        above_average_count += 1

print("Marks:", marks)
print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Average mark:", average)
print("Number of students scoring above average:", above_average_count)