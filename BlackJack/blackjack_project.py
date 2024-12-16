from logo import logo
import random
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
    
def calculate_score(cards):

    if sum(cards) == 21:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Opponenet has BlackJack"
    elif user_score == 0:
        return "Win win a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponnent went over. You win"
    elif user_score> computer_score:
        return "You win"
    else:
        return "You Lose"

def play_game():

    print(logo)

    user_cards = []
    computer_cards =[]
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your card : {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score> 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'Y; to get another card, type 'N' to pass")
            if user_should_deal == "Y":
                user_cards.append(deal_card())
            else:
                is_game_over == True

    while computer_score!=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#! Ask the user if they want to play the game from all over again

while input("Do you want ot play the game again? 'Y' or 'N'") == 'y':
    os.system('clear')
    play_game()