monday_temperatures = [9.1, 8.8, 7.6]

for temp in monday_temperatures:
    print(round(temp))
print("DONE")

for letter in "hello":
    print(letter.upper())

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int) and color > 50 :
     print(color)

def celsius_to_kelvin(cels):
    return cels + 273.15
 
for temperature in [9.1, 8.8, -270.15]:
    print(celsius_to_kelvin(temperature))

student_grades = {"Marry": 9.1, "John": 8.8, "Alice": 7.5}
for grade in student_grades.items(): #values() returns the values of the dictionary #items() returns the key-value pairs
    print(grade)


phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
for pair in phone_numbers.items():
    print(f"{pair[0]} has as phone number {pair[1]}")
 
for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}")

dict_private = {"John Smith": +37682929928, "Marry Simpons": +423998200919}
for name, phone in dict_private.items():
    print(f"{name} : +{phone}")

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for phone in phone_numbers.values():
    print(phone.replace("+", "00"))

for i in [1, 2, 3, 4, 5]:
    print(i * 2)

a =3 
while a < 10: # while loop: is executed if the condition is true
    print(a)
    a += 1

user_name = ' '
while user_name != "pypy": # while loop: is executed if name is not equal to "pypy"
    user_name = input("Enter your name: ")

while True: # infinite loop
    userName = input("Enter your name: ")
    if userName == "pypy":
        break # break statement to exit the loop
    else:
        print("Try again!")
        continue # continue statement to skip the rest of the loop and start from the beginning
 

for letter in 'abc':
    print(letter.upper())