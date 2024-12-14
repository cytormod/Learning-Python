programming_dictionary = {
    "Bug": "An errot in a program that prevenets tha program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": 'The action of doing something over and over again.',
}

# print(programming_dictionary["Bug"])
programming_dictionary['Joke'] = "The first programm was died because it was executed"

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}

# Edit an item in Dictionary
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
    # print(key)
    # print(programming_dictionary[key])

# Grading Program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    score = student_scores[key]
    if score > 90:
        student_grades[key] = "Outstanding"
    elif score > 80:
        student_grades[key] = "Exceeds Expectations"
    elif score > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = 'Fail'
         
# print(student_grades)

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting Dictionary into a Dictionary

cities_visited = {
    "Visited" : {
        "France": ["Lille", "Dijon"],
        "Germany": "Berlin",
        "total_visits": 3, 
    },
    "Not_Visited" : {
        "France" : "Paris",
        "Germany": ["Stuttgart", "Hamburg"],
        "total_non-visit": 3
    }
}

# Nesting Dictionary in a List + Challenge

travel_log2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]


def add_new_country(country, total_visits, cities):
    new_country = {}
    new_country['country']= country
    new_country['cities_visited']= cities
    new_country['total_visits']= total_visits
    travel_log2.append(new_country)
    

add_new_country("Russia", 7, ["Moscow", "Saint Petersburg", "Rostov-On-Don", "Tula", "Novocherkassk", 'Tomsk', 'Kamen-Shaktinsk'])

print(travel_log2)