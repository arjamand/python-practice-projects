# 2022-11-05 16:26:51

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import quiz_brain
question_bank = []
n = 0
for q in question_data:
    text = question_data[n]["question"]
    answer = question_data[n]["correct_answer"]
    question_object = Question(text, answer)
    question_bank.append(question_object)
    n += 1
#    print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_have_a_question() != False:

    # print(quiz_brain.score)
    quiz.next_question()
    # quiz.check_answer()
print("\nYou have completed the quiz")
print(f"Your score is {quiz_brain.score}/{quiz.question_number} .\n")
