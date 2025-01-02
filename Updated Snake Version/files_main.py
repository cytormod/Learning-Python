# file = open('my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

# Most of the Python developer uses with keyword so that they don't have to remember to close the file 'file.close()' and here how it works

with open('my_file.txt') as file:
    contents = file.read()
    print(contents)

# ------------ to Write the file------------ #

# mode  = w ===> "Means it will overwrite the new data"
# mode  = a ===> "Means it will add the new data into the existing note"

with open('my_file.txt', mode='a') as file:
    file.write("\nNew Text.")

# If you don't have some file or you want ot create the file automatically, we can also use the mode of 'w'
with open('New_file.txt', mode='w') as file:
    file.write("New Text.")

