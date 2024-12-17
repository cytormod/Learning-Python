import random
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    '''checks answer against guess. Returns the number of turns remaining'''
    if guess>answer:
        print("Too HIGH")
        return turns - 1
    elif guess < answer:
        print("Too LOW")
        return  turns - 1
    else:
        print(f"You got it. The asnwer was {answer}")

def set_difficulty():
    level = input("choose a difficulty. Type 'easy' or 'hard'")
    if level =='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("welcome to the guessing Game")
    print("I'm thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    print(answer)

    turns = set_difficulty()

    guess = 0
    while guess!= answer:
        print(f"You have {turns} attempts remaining to guess the number.") 
        guess = int(input("Make a guess"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("Youhave run out of the guessses you loose")
            return
        elif guess != answer:
            print("Guess again. ")
game()












