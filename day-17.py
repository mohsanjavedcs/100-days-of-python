from _question_model import Question
from _data import question_data
from _quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    statement = question["text"]
    answer = question["answer"]
    new_question = Question(statement, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")