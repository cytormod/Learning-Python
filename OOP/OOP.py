# import another_module
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable() #accessing the class Name or creating the new Object name table using the blueprint PrettyTable()
print(table)

table.add_column('Pokemon', ["Pikachu", "Charmandor", "Squirtle"])
table.add_column('Type', ["Electric", "Water", "Fire"])
table.align = "l" #Changing alignment with the attribute align
print(table)
