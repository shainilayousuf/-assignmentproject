#6.4
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)
#6.5
river = { "nile" : "Egypt" , "Amazon" : "South America" , "Satlaj" : "Pakistan" }
for key , value in river.items():
    print("The "  +key.title()+ " runs through " +value.title())
favorite_languages = {
    'shainila': 'python',
    'mariam': 'c',
    'sundas': 'java',
    'komal': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("\n")

coders = ['komal', 'ali', 'mariam', 'adeel', 'shainila', 'sara', 'tooba']
for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")
#6.7# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'shainila',
    'last_name': 'yousuf',
    'age': 18,
    'city': 'karchi',
    }
people.append(person)

person = {
    'first_name': 'mairam',
    'last_name': 'bilal',
    'age': 20,
    'city': 'karachi',
    }
people.append(person)

person = {
    'first_name': 'ali',
    'last_name': 'khan',
    'age': 8,
    'city': 'karachi',
    }
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(name + ", of " + city + ", is " + age + " years old.")
   #6.8# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
cat = {"Persian"  ,  "Sarah"}
dog = {"Bull Dog"  ,  "Peter"}
snake = {"Python"  , "Harry"}
parrot = {"Macaw"  ,  "Suzain"}
pets = [ cat  ,  dog  ,  snake  ,  parrot]
for info in pets :
    print (info)
  #6.9
favorite_places = {
    'shainila': ['saudi arabia', 'china', 'india'],
    'mariam': ['saudi arabia', 'canada'],
    'sundas': ['iran', 'saudi arabia', 'japan']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())
 #6.10
        favorite_numbers = {
            'zarar': [42, 17],
            'adeel': [42, 39, 56],
            'shainila': [7, 12],
        }

        for name, numbers in favorite_numbers.items():
            print("\n" + name.title() + " likes the following numbers:")
            for number in numbers:
                print("  " + str(number))
#6.11

cities = {

    "karachi": {

        "country": "Pakistan" , "population": "21.2 million", "fact": "Ecnomical Hub",
    },

    "islamabad": {

        "country": "Pakistan" , "population": "1.152 million", "fact": "Capital city of Pakistan",
    },

    "lahore": {

        "country": "Pakistan", "population": "11.13 million", "fact": "Heart of Pakistan",
    },
    }
for key, value in cities.items():

    a = value["country"]
    b = value["population"]
    c = value["fact"]
    print("City = " +key.title()+ " , Country : " +a+ " , Population " +b+ " , Fact  " +c)
