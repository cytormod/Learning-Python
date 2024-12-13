import random
import hangman_words
from hangman_logo import logo

chosen_word = random.choice(hangman_words.word_list)
word_length  = len(chosen_word)

end_of_game = False
lives = 6
stages = ['6', '5', '4', '3', '2', '1']

#Step 1
print(logo)
print(chosen_word)

# print(f"the solution is {chosen_word}")

display = []
 
#  Setup to get blank
for _ in range(word_length):
    display += "_"
print(display)


# While will continue to give loop until our balnks get finished
while not end_of_game:
    # Guessing the letter
    guess = input("Guess the letter.\n").lower()

    # if user is repeating the letter again, warn them
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        print('letter ' + letter)
        print(position)
        if letter == guess:
            display[position] = letter
    print(display)
    # Reducing the lives if there is wrong guess
    if guess not in  chosen_word:
        print(f"Your guess is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")
            print(f"The word was {chosen_word}")

    # If every blanks get filled, show You Win
    if "_" not in display:
        end_of_game = True
        print('You Win')

    print(stages[lives])
