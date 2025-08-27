def weather_conditional(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "It's a cold day."
    

#userInput = float(input("Enter the temperature: "))
#print(type(userInput))
#print(weather_conditional(userInput))}

user_name = input("Enter your name: ")
user_surname = input("Enter your surname: ")
when = "today"
message = "Hello %s %s, welcome to the program!" % (user_name, user_surname) #for printing use %s and %  for strings
message = f"Hello {user_name} {user_surname} welcome to the program! What´s {when} up?" #other way to print is using f-string that is more modern
print(message)

name = "John"
surname = "Smith"
message = "Your name is {}. Your surname is {}".format(name, surname)#This is another way to print using format {} . format() method
print(message)


def fooName(namePerson):
    if namePerson:
        namePerson = namePerson[0].upper() + namePerson[1:].lower()
        return f"Hi {namePerson}"

print(fooName("juancho"))
