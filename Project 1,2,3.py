# print("Hello "+input("what is your name?"))
# print(len(input("what is your name")))

#! 014 Variables

# a = input("a: ")
# b = input("b: ")


# c = a
# a = b
# b = c
# print(c, b)

#! Project 2
 
# a = (input('write two Numbers: '))
# frst = a[0]
# scnd = a[1]
# print(int(frst) + int(scnd))

# print(round(8/3, 2))
# print(type(8 // 3)) #It will automatically do the floor of the result

# # f-string
# score = 1
# print(f"your score is {score}")

# !How many days left task

# age = input("What is your current age?")
# remaining_age = 90 - int(age)
# days_left = remaining_age * 365
# week_left = remaining_age * 52
# month_left = remaining_age * 12
# print(f"your remaining age is {remaining_age}, you have {days_left} days, {week_left} weeks, and {month_left} months left")


#! Challenge Tip Calculator
# print('Welcome to the tip Calculator')
# total_bill = input('What is the total bill?')
# total_percentage_tip = input('What percentage tip would you like to give? 10, 12, 15')
# distribution = input('How many people to split the bill? ')

# int_bill = int(total_bill)
# int_percentage_tip = int(total_percentage_tip)
# int_distribution = int(distribution)
# final_calculation = ((int_percentage_tip/100) * int_bill)
# add_tip = ((int_bill + final_calculation)/int_distribution)
# # print(type(final_calculation), final_calculation)

# print(f'Each person should pay{add_tip}')

#! Project 3

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))

# if height >= 120:
#     print('you can ride the rollercoaster!')
#     age = int(input('What is your age?'))
#     if age <= 12:
#         print('Please pay $5.')
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print('Please pay $12.')
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# # ! Challenge Odd or Even

# number = int(input("which number do you want to choose"))

# if number % 2 == 0: 
#     print("It is the even Number")

# else:
#     print("It is the odd number")

# # BMI Challenge
# height = float(input('enter your height in m: '))
# weight = float(input("enter your weight in kg: "))
# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#     print(f"Your bmi is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your bmi is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your Bmi is {bmi}, you are overweight.")
# else:
#     print(f"your bmi is {bmi}, you are clinically obese.")

# ! Leap year calender
# year = int((input("Which year do you want to check?")))

# if year % 4 ==0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("it's a Leap year")
#         else:print("It's not a leap year")
#     else: print("It's a leap Year")
# else: print("It's not a leap year")

# you can ride with this amount of Prize
# height = (int(input("Height")))
# bill = 0
# if height > 120:
#     print('you can ride')
#     age = int(input("Age?"))
#     if age < 12:
#         bill = 5
#         print("$5")
#     elif age <=18:
#         bill = 7
#         print("$7")
    # elif age>=45 and age<=55:
        # print('$0')
#     elif age > 18:
#         bill = 12
#         print("$12")

#     photo = input("Do you want to photo taken? Y or N")

#     if photo == "Y":
#         bill += 3

#     print(f"Your final bill is {bill}")

# else: print("Not Allowed")

#? Pizza app

# print('welcome')
# size = input("Size Pizza? S, M, or L")
# add_pepperoni = input("Want pepperoni? Y or N")

# extra_cheese = input("Want Cheese? Y or N")
# add_bill = 0

# if size == "S":
#     add_bill = 15
#     print("$15")
# elif size == "M":
#     add_bill = 20
#     print("$20")
# elif size =="L":
#     print("$25")


# if add_pepperoni == "Y":
#     if size == "S":
#         add_bill +=2
#     else:
#         add_bill += 3

# if extra_cheese== "Y":
#     add_bill +=1
# print(f"Your Final Bill is ${add_bill}")

# Logical Operator

#? AND Operator (Both of the value has to be true)


#? OR Operator (Any one condition needs to be true, when both of the statement are false the whole statement will become FALSE)


# ? NOT Operator (It reverses the Condition)

# Calculator

# print("Love calculator")
# name1 = input("What is your Name? \n")
# name2 = input("What is their name? \n")

# combined_string = name1+name2
# lower_case_string = combined_string.lower()
# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")

# true =  t+r+u+e

# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")

# love = l+o+v+e

# love_score = int(str(true) + str(love))


# if (love_score < 10) or (love_score > 90):
#     print(f"Your Love Score is {love_score}, you go like mentos and Cola")
# elif (love_score >= 40) and (love_score<=50):
#     print(f"Your score {love_score}")
# else:
#     print(f"Your Score is {love_score}")

# ? Project Treasure Island

# print("Welcome to Treasure Island. Your Mission is to find the Treasure")

# direction = input(print("left or Right?"))


# if(direction == "Left"):
#     crossing = input(('swim or wait?'))
#     if crossing == 'Wait':
#         door = input(print("Which Door? Red, Blue or Yellow?"))
#         if (door == 'Red'):
#             print('it is a room full of fire. Game Over.')
#         elif (door == 'Yellow'):
#             print('You have found the treasure! You win')
#         elif (door == 'Blue'):
#             print('You enter a room of Beast. Game Over')
#         else: print('You have chose a door that does not exist')
#     else:
#         print('You got attacked by an angry Trout')

# else:
#     print('You fell into a hole. Game Over')


# ! CHECK ASKPYTHON.COM 




