import random
import my_module
# ! YOUTUBE: PSEUDORANDOM NUMBER GENERATORS

# ? WEBSITE: ASKPYTHON.COM

# random_integer = random.randint(1, 10)
# print(random_integer)
# print(my_module.pi)

# # Float : 0.00000 - 0.99999
# random_float = random.random()
# print(random_float)

# randomFloat = random.random() * 5
# print(randomFloat)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# random.randint(0, 1)
# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails ")

# ? List is also

# states_of_germany = ['Baden-Wurttemberg', 'Bavaria', 'Berlin', 'Brandenburg', 'Bremen', 'Hhamburg', 'Hesse', 'Mecklenburg-Vorpommern', 'Lower Saxony', 'North Rhine-Westphalia', 'Rhineland-Palatinate', 'Saarland', 'Saxony-Anhalt', 'Schleswig-Holstein', 'Thuringia']

# print(states_of_germany[2])
# states_of_germany[1] = 'Pennsylvaniya'

# states_of_germany.append("Sahil")
# states_of_germany.extend(["America", 'Russia', 'India   '])

# ? FLip The Coin

# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else: print('Tails')

# ? Who is going to pay the Bill
# solit string method
# names_string = input("Give me everybody's name, seperated by a Comma.")
# names = names_string.split(",")

# num_items = len(names)
# random_choice = random.randint(0, num_items -1)
# person_who_will_pay = names[random_choice]
# print(f"{person_who_will_pay} is going to buy the meal today")

# ! 4-006 Working with nested list
# fruits = ["Strawberries", 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
# vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

# ? Treasure Map Challenge 
row1 = ['_', '_', '1']
row2 = ['_', '_', '_']
row3 = ['2', '_', 'vh']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure?")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = (map[vertical-1])
selected_row[horizontal -1]="X"
print(f"{row1}\n{row2}\n{row3}")

# ? Rock Paper Scissors
print('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.')

rock = ["It's Rock"]
paper = ["It's Paper"]
scissor = ["It's Scissor"]

# # For Computer
# map = [rock, paper, scissor]
# computer_selection = random.randint(0, len(map))
# print(map[computer_selection-1])

# For person
game_images = [rock, paper, scissor]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
print(game_images[user_choice])
computer_choice = random.randint(0,2)

print(f"Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice<0:
    print("you types an invalid number, you lose!")
elif user_choice ==0 and computer_choice== 2:
    print("You wins")
elif(computer_choice == 0 and user_choice ==2):
    print('You lose')
elif(computer_choice > user_choice):
    print("You Lose!")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice == user_choice:
    print("It's a draw")

























