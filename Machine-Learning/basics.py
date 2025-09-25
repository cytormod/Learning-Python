# import os
# import pandas as pd

# # os.system("cat /proc/cpuinfo")
# # os.system("cat /proc/meminfo")
# df = pd.read_csv('def91b5553736764e8e08f6255390f37/BostonHousing.csv')
# print(df.head())

print ('hi')

# Variables and input

greeting = "Hello"
print("Enter your name:")
# name = input()
question = "How are you?"
# print(greeting + " " + name + " " + question)

# Numeric variables

width = 15
length = 22

print(type(width))
print(type(length))

area = width * length

print("Area of land: " + str(area))

# === 

# name = input()

hund = 100
# age = int(input())
# print(type(age))
# remaining_years = hund - int(age)

# print("Hello " + name + " You will live more " + str(remaining_years) + " till 100")
# to check
# In python everything is an object

# ---- Boolean

value = True
print(value)
print(type(value))
name = input("Enter youe name: ")
# if True:
#     print("True")
# print("Program finished.")

# if name == "Sahil":
#     print("Your name is Sahil")
# else:
#     print("Your name is not in our DataBase")

# print('Program finished')

# ! For constants
NAME = "Sahil"
if name == NAME:
    print("Your name is " + NAME)

WORKER1 = 'Sahil'
WORKER2 = 'K9'
WORKER3 = 'Cai'

if name == WORKER1:
    print("You are your own Boss")
elif name == WORKER2:
    print("Sounds like game, So play it with Life")
elif name == WORKER3:
    print("Let you work for it to make it extend by TorIty")
else:
    print("Everything has some purpose here")

# Comparison Operators
# ==, <, >, !=, <=, >=
# UNICODE TABLE
print(ord("c"))
print(ord("D"))

print("cat" > "Dog")

# FOR Loops
print('FOR Loop')

for i in range(4):
    print('Hello ' + str(i))

for i in range(1, 4):
    print(i)

# Range also has step size 3 parameter
for i in range(4,11, 2):
    print(i)

# _ to ignore variable
for _ in range(3):
    print("Hello")

# Indentation

for i in range (3):
    print(i)

    if i == 2:
        print("i is 2")


# Break

for i in range(5):
    print("Starting loop Number " + str(i))

    stop = input("Stop the loop (y/n) ? ")
    if stop == "n":
        continue
    elif stop == 'y':
        break

    print("Ending loop number " + str(i))

print("Program finished")

"""
Write a program that asks the user to enter a password and compares it to a hard-coded password.

if the password is correct the programm prints "Welcome to the EMPIRE"

If the passwoed is cinorrect, the program prints "Access denied" and then asks for the password again.

The program will ask for the password three times if necessary.

After that, it exits.

"""

PASSWORD= str(123) 


for i in range(3):
    user_pass = input("Enter password: ")

    if user_pass == PASSWORD:
        print("Welcome to the EMPIRE")
        break
    else:
        print('Access Denied')

# Boolean Operator
# and, not, or

is_raining = True
is_windy = False

stay_inside = is_raining and is_windy

print('stay inside: ' + str(stay_inside))

take_coat = is_raining or is_windy
print("take a coat: " + str(take_coat))

"""
Ask the user:
1. Are you a student?
2. Do you have pets?
3. Do you smoke?

The program automatically decides whrther a property you've applied to rend is available to you.

It should print an appropriate response, like "Property Available" or "Property unavailable".

The program applies these criteria:

if you're a student, you can only rent the property if you don't have pets and don't smoke
If you're not a student, you can rent the property if you smoke or have pets, but not if you both smoke and also have pets.
"""

is_student = input("Are you a Student? ") == "y"
has_pets = input('Do you have pets? ') == "y"
does_smoke = input("Do you smoke ") == "y"

# ! Mistake in the 2nd part of code, it was a logic test

# if is_student and not has_pets and not does_smoke:
#     print("Available")

# if not is_student and does_smoke or has_pets:
#     print("Not Available")

# !!!!

student_can_rent = is_student and not has_pets and not does_smoke
non_student_can_rent = not is_student and not (does_smoke and has_pets)

print(student_can_rent)
print(non_student_can_rent)

can_rent = student_can_rent or non_student_can_rent

# While

password = ""

while password != PASSWORD:
    password = input("Enter Password: ")

print("Access Granted")