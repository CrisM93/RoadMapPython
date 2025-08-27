#Continuamos renombrando el nombre de program a nombre de la seccion en un inicio fuerron my_program....
# More about de functions in python https://docs.python.org/3/tutorial/controlflow.html#defining-functions

def area_of_square(sideA, sideB):
    return sideA * sideB

print(area_of_square(sideB=20, sideA=5))  # Output: 25


def concat_strings(str1, str2):
    return str1 + " " + str2
print(concat_strings("Hello", "World"))

def avarage_fuction(*args):#here we can pass any number of arguments
    return sum(args) / len(args)

print(avarage_fuction(10, 20, 30, 40, 50))  

def string_sorter(*args):
    return sorted(arg.upper() for arg in args)

print(string_sorter("banana", "apple", "cherry"))

def maeni(**kwargs):
    return kwargs
print(maeni(name="Alice", age=30, city="New York")) #this print the dictionary ['name': 'Alice', 'age': 30, 'city': 'New York']

def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=3, b=3, c =3))