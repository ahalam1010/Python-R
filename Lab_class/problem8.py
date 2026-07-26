student_marks = {
    "Nina": 78,
    "Labubu": 85,
    "Susa": 67,
    "Shane": 85,
    "Nadia": 55
}

total_marks = 0
student_count = 0
highest_mark = None
highest_students = []

print("Student marks:")

for student, mark in student_marks.items():
    # (a) Display each name and mark
    print(student, ":", mark)

    # Used for calculating average
    total_marks += mark
    student_count += 1

    # (c) Find the highest mark and all tied students
    if highest_mark is None or mark > highest_mark:
        highest_mark = mark
        highest_students = [student]

    elif mark == highest_mark:
        highest_students.append(student)

# (b) Calculate class average
class_average = total_marks / student_count

print("\nClass average:", class_average)
print("Highest mark:", highest_mark)

print("Student(s) with the highest mark:")

for student in highest_students:
    print(student)

# (d) Display students scoring at least 60
print("\nStudents scoring at least 60:")

for student, mark in student_marks.items():
    if mark >= 60:
        print(student, "-", mark)