print(2+9)

spent = 3
donated =4
#----Comentarios de esta manera
total_amount = spent * donated
print(total_amount)

x=10
y ="hola"
z=1.1
sum1= x+x
sum2= y+y
print(sum1)
print(sum2, z)
print("\n")

students_grades = list(range(7,17,3))
print(students_grades)

students_uni = [87.1, 8.7, 7.5]
print(sum(students_uni))
print(len(students_uni))
print(max(students_uni))

student_grad = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(student_grad.count(10.0))

username = "Python3"
print(username.upper())
print(username.lower())
students_gradess = {"Juan":10, "Pedro":45, "Maria":10}
print(students_gradess)
print("Suma de calif:", sum(students_gradess.values()))

monday_temperatures=(1,2,3) #unmutable
wends_temperatures=[1,2,3] #mutable
wends_temperatures.append(7)
print(wends_temperatures)
#Dictionary Key-Value
day_temperatures ={"morning":(1.1, 2.2,3.3), "noon":(1.1, 2.2,3.3), "evening":(1.1, 2.2,3.3)}


print("todaii".replace("i", "y"))
x =[1, 2,   3]

turdays_temperatures=[9.1, 8.8, 7.5]
turdays_temperatures.append(8)
print(turdays_temperatures)
turdays_temperatures.clear()#Limpia la lista
print(turdays_temperatures)
turdays_temperatures.append(8.8)#agrega a la lista
print(turdays_temperatures)
turdays_temperatures.append(9.8)#agrega a la lista
print(turdays_temperatures.index(8.8))#se busca la  posicion del dato ingresado
print(turdays_temperatures)
turdays_temperatures.append(9.8)#agrega a la lista

seconds = [1.23, 1.45, 1.02, 1.11]
seconds.remove(1.45)

seconds = [1.23, 1.45, 1.02, 1.11]
seconds.remove(1.45)
seconds.remove(1.02)
seconds.remove(1.11)

man_temperatures=[7.7,8.8,9.9,13,4]
print(man_temperatures.__getitem__(0))

workdays = ["Mon", "Tue", "Wed", "Thu", "Fri", 2]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
print(workdays)
print(len(workdays))#imprime el tamaño de la lista workdays
print(workdays[0:3])#imprime por indices
print(workdays[:3])#imprime por indices
print(workdays[-2])#imprime de ultimo hacia el primero negaivamente

myString = "cris"
print(myString[0])
print(workdays[0][0])#accede al arreglo el indece 1 es la posicion del elemento mientras en 2 es el indice del string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[0:3])
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[4:7])

#dictionaries
student_grady={"Juan":10, "Pedro":20, "Martu":40}
print(student_grady["Juan"])
eng_port = {"rain":"chuva", "sun":"sol"}
print(eng_port["rain"])
