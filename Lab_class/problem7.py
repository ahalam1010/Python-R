student = {
    "name": "Ahlam",
    "id": "220039",
    "program": "Computer Science",
    "year": 3
}

# (a) Display the original dictionary
print("Original dictionary:")
print(student)

# (b) Update the year of study
new_year = int(input("Enter the new year of study: "))
student["year"] = new_year

# (c) Add an email key
email = input("Enter the student's email: ")
student["email"] = email

# (d) Display every key and value
print("\nUpdated student profile:")

for key, value in student.items():
    print(key, ":", value)

# (e) Check whether phone exists
if "phone" in student:
    print("\nThe key 'phone' exists.")
else:
    print("\nThe key 'phone' does not exist.")