# Create a list of student names and perform list operations.

students = ["Ahlam", "Nadia", "Sara", "Mariam"]

print("Original list:", students)

students.append("Fatima")
print("After adding a new student:", students)

students.insert(1, "Lamia")
print("After inserting a student at position 2:", students)

students.remove("Sara")
print("After removing a student:", students)

students.sort()
print("After sorting alphabetically:", students)