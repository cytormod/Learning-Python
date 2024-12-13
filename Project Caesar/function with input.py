import math
import Caesorlogo

print(Caesorlogo.logo )

def greet():
    print("hello")

# Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}")

greet_with_name("Sahil")

# function with more than 1 inputs
def greet_with(name, location):
    print(f"Hi {name}, are your from {location}?")
    print(f"What is it like in {location}")

greet_with('Sahil', "Berlin")

# Wall painting
# ! Area Calculation

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

# number_of_cans = 0
# def paint_calc(height, width, cover):
#     # height = test_h
#     # width= test_w
#     # cover = coverage
#     # calc = (height*width) / cover
#     area = height*width
#     num_of_cans = math.ceil(area/cover)
#     print (f"You will need {num_of_cans} paint")

# paint_calc(height=test_h, width=test_w, cover= coverage)

# ! Prime Number Checker
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a Prime Number.")
#     else:
#         print("It's not a prime Number.")
# n = int(input("Check this number"))
# prime_checker(number = n)

#!  Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#         # print(position)
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#         # print(position)
#     print(f"The encoded text is {plain_text}")

# if direction == "Encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "Decode":
#      decrypt(cipher_text= text, shift_amount=shift)
# else:
#     print("Choose the correct direction" )

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "Decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)        
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
             end_text += char
    print(f"The {cipher_direction} text is {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'Encode' to encrypt, type 'Decode' to decrypt:")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift%26

    caesar(start_text = text, shift_amount = shift, cipher_direction=direction) 
    result = input("Type 'Y' if you want to go again. Other type 'N'.\n")
    if result == 'N':
         should_continue = False
         print("Goodbye")