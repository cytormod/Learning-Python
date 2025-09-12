#!/home/sahil-gopani/Desktop/JS/Learning-Python/Machine-Learning/venv/bin/python
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

name = input()

hund = 100
age = int(input())
print(type(age))
remaining_years = hund - int(age)

print("Hello " + name + " You will live more " + str(remaining_years) + " till 100")