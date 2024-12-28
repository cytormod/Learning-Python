from Data import question_data
from question_class import Question
from quiz_brain import QuizBrain

class User:
    def __init__(self, user_id, username):

        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0
        print('I am inside in_it class')

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("001", "Sahil")
print(user1)
user2 = User("002", "Gopani")
user1.follow(user2)
print(User)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)


# ------------------------------------------------QUIZ APP--------------------------------------------------

question_bank = []
for question in question_data:
    question_text = question["text"]
    # print(question_text)
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# ! OPENTRIVIADATABASE = Opentrivadb