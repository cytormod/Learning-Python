import random
import os

enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# ! Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength) # Because it is outside the LocalScope it won't be able to work

# ! Global Scope
player_health = 10
def game():
    def drink_potion():
        potion_strength =2
        print(player_health)
    drink_potion()
print(player_health)

#There ia no blok scope
game_level = 3
def create_enemy():
    enemies = ["skeleton", "zombies", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)
# print(new_enemy) # it is outside of our scope 

#! Modifing Global Scope

enemies = 1
def increase_enemies():
    # Don't try to modify the function inside the scope, it prones to give you Bugs: You can read it like we are doing in the print fncn
    # global enemies
    # enemies += 1 # ! We have mentioned the word Global before to tell the function that we are trying to modify the global Varivale, which we have defined before
    print(f"enemies inside function: {enemies}")

    # ! So How can we change our Global Variable?
    #! BY RETURNING IT

    return enemies + 1

# increase_enemies()

enemies = increase_enemies()

print(f"enemies outside function: {enemies}")

# Python Constants and Global Scope
# The naming convention for constants will all change to uppercase() ->

PI = 3.1415
URL = 'https://www.google.com'
TWITTER_HANDLE = "@Cyor"

# def calc():
#     TWITTER_HANDLE = "@hi"# Here it will automaticaly reminds us to not to change the constant variable

# ! Guessing Game
# print("Welcome to the number Guessing Game")
# print("I am thinking of a number between 1 -100")
choosing = int(input("Choose the difficulty type. Type '1' for 'easy', '2' for 'hard'"))

hard_mode = 5
easy_mode = 10

def game_process():
    computer_guessed_number = random.randint(1, 100)
    print(computer_guessed_number)
    users_guess = int(input('Make a guess'))
    if users_guess < computer_guessed_number:
        print ("Your guess is too LOW, Make HIGH Guess")
    elif users_guess > computer_guessed_number:
        print ("Your guess is too HIGH, Make a LOW Guess")
    elif users_guess == computer_guessed_number:
        print("Your won, you've guessed correctly")

def guessing_start():
    guessed = True
    if choosing == 1:
        print("You will get 10 chances to guess the answer")
        while not guessed:
            game_process()
            guessed = False
    elif choosing == 2:
        print("You will get 5 chances")
guessing_start()





