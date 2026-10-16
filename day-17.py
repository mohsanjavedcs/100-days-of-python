from _question_model import Question
from _data import question_data

question_bank = []

for question in question_data:
    statement = question["text"]
    answer = question["answer"]
    new_question = Question(statement, answer)
    question_bank.append(new_question)