class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number == 12:
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number = self.question_number + 1
        user_ans = input(f"{self.question_number} : {current_question.text} (trues/false) :")
        self.check_answer(user_ans, current_question)

    def check_answer(self, user_ans, current_question):
        if current_question.answer.lower() == user_ans.lower():
            print("You Got It Right !!")
            self.score += 1
        else:
            print("OOPS ! Wrong Answer ")

        print(f"THE CORRECT ANSWER IS {current_question.answer.lower()}")
        print(f"Your current score is {self.score}")





