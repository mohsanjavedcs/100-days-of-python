student_scores = {
    "Ali": 81,
    "Ahmed": 93,
    "Ahsan": 74,
    "Ameer": 48,
    "Abdullah": 90,
}

student_grades = {}

for student in student_scores:
    if student_scores[student] >= 91:
        student_grades[student] = "Outstanding"
    elif student_scores[student] >= 81 and student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71 and student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    elif student_scores[student] <= 70:
        student_grades[student] = "Fail"

print(student_scores)
print(student_grades)