import random
import os
import logo
from game_data import data

# print (logo)
# print("Compare A: Neymar a Football Player, from Brazil")

# list = data
# # print(list[1]['name'])
# name_list =[]
# followers_count = []

# def extraction(extraction_part, part_to_append):

#     for key in list:
#         names = key[extraction_part]
#         # print(names)
#         part_to_append.append(names)

# extraction('name', name_list)
# extraction('follower_count', followers_count)
# print(name_list, followers_count)


# print(random.choice(name_list))

def format_data(account):
    '''Takes the account data and returns the printable format'''
    account_name = account['name']
    account_descr = account["description"]
    account_country = account['country']
    print(f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
    '''Take the user guess and follower counts and return if they got it right.'''
    if a_followers > b_followers:
        if guess == "a":
        #     return True
        # else:
        #     return False
            return guess == 'a'
        else:
            return guess =='b'

print(logo)
score = 0

game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(f"Against B: {format_data(account_b)}.")


    guess = input("who has more followers? Type 'A' or 'B': ").lower()

    # Getting follower account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # os.system('clear')
    print(logo.logo)

    if is_correct:
        score += 1
        print(f"You're Right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, You're Wrong. Final score: {score}")




