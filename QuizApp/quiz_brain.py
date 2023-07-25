score = 0


class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0

    def still_have_a_question(self):
        if self.question_number == len(self.question_list):
            return False

    def next_question(self):

        q = self.question_list[self.question_number]
        self.question_number += 1
        option_1 = input(
            f"Q.{self.question_number}: {q.text} (True/False): ")

        self.check_answer(option_1, q=q)

    def check_answer(self, option_1, q):
        # next_question.score=0
        global score
        if (option_1).lower() == (q.answer).lower():
            score += 1
            print("You got it right !")
        else:
            print("You got it Wrong !")
        print(f"The Correct answer was : {q.answer} . ")
        print(f"Your score is : {score} of {self.question_number}")
