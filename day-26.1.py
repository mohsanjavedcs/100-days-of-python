import random

students = ["Mohsan", "Ali", "Shahbaz", "Zainab"]
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

squared_numbers = [n**2 for n in numbers]

result = [n for n in numbers if n % 2 == 0]

student_scores = {
    student: random.randint(0, 100) for student in students
    }

passed_students = {
    student: score for (student, score) in student_scores.items() if score >= 60
    }

result = {
    word: len(word) for word in sentence.split()
}