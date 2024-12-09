import random

# fruits = ["Apple", 'Peach', 'Pear']
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie ")

# # ! Average height Exercise
# student_heights = input("input a list of students heights: ").split()
# # for n in range(0, len(student_heights)):
# #     student_heights[n] = int(student_heights[n])
# # print(student_heights)

# total_height = 0;
# for height in student_heights:
#     total_height+=height
#     # print(total_height)


# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
#     print(number_of_students)

# average_height = round(total_height / number_of_students)
# print(average_height)

# ! HIghest_Scoore
# student_scores = int(input("Input a list of student score"))
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
#         # print(highest_score)
# print(f"The highest score in the class is: {highest_score}")

# print(student_scores)

# !005 For Loop and the Range()
# for number in range(1, 10, 3) :
#     print(number)

# total = 0
# for number in range(1, 101): 
    # total += number
# print(total)

# ! 006 Sum of all even numbers
# total = 0
# for number in range (2, 101, 2):
#   total += number
# print(total)

# total2 = 0
# for number in range(1, 101):
#   if number%2==0:
#     print(number)
#     total2 += number
# print(total2)

# ! 007 FizzBuzz
# for number in range (1, 100):
#     if(number%15==0):
#         print('FizzBuzz')
#     elif(number%5==0):
#         print('Buzz')
#     elif(number%3==0):
#         print('Fizz')
#     else:
#         print(number)

# for number in range(1, 100):
#     if(number % 3 == 0 and number%5==0):
#         print('FizzBuzz')
#     elif(number%5 ==0):
#         print('Buzz')
#     elif(number%3==0):
#         print('Fizz')
#     else:
#         print(number)

# !008 Password Generator Random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')','*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level
#fghf*&23

#Hard Level
# f*f238*9390f*kjtk

# print(nr_letters)
# print(nr_symbols)
# print(nr_numbers)

#! print random letters
randomLetters =''
for nr_letter in range(1, nr_letters+1):
    randomLetters += random.choice(letters)

#! Print random Symbols
randomSymbols = ''
for nr_symbol in range(1, nr_symbols+1):
    randomSymbols += random.choice(symbols)

#! print random Numbers
randomNumbers = ''
for nr_number in range(1, nr_numbers+1):
    randomNumbers += random.choice(numbers)

sequence_rn = randomNumbers+randomLetters+randomSymbols
print(sequence_rn)

final_random = ''
for randomPass in range(1, len(sequence_rn)+1):
    final_random += random.choice(sequence_rn)
print(final_random)

# random_rn = random.check(sequence_rn)
# print(sequence_rn)
# print(random_rn)




























