student_marks = [
    {"id": "S101", "name": "Amina", "marks": [78, 84, 69]},
    {"id": "S102", "name": "Bina", "marks": [55, 61, 58]},
    {"id": "S103", "name": "Chen", "marks": [91, 88, 95]},
    {"id": "S104", "name": "Dipa", "marks": [42, 49, 46]}
]


def prepare_results(students):
    results = {}

    for student in students:
        marks = student["marks"]
        total = 0

        for mark in marks:
            total += mark

        average = total / len(marks)

        if average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        results[student["id"]] = {
            "name" : student["name"],
            "average" : round(average, 2),
            "grade" : grade
        }

    return results

final_results = prepare_results(student_marks)

for student_id, info in final_results.items():
    print(
        "ID:", student_id,
        "Name:", info["name"],
        "Average:", info["average"],
        "Grade:", info["grade"]

    )

grade_frequency = {}

for student_id, info in final_results.items():
    grade = info["grade"]

    if grade in grade_frequency:
        grade_frequency[grade] += 1
    else:
        grade_frequency[grade] = 1

print("Grade frequency: ", grade_frequency)