#Funciones

def mean(mylist):
   the_mean = sum(mylist)/len(mylist)
   return the_mean
print(type(mean), mean([1,2,3]), "tamanio lista=", len([0,1,2]))

def convert(amount):
    output = amount * 1.75
    return output
print(convert(10))

def squareArea(lado):
    areaS = lado * lado
    return areaS
print(squareArea(3))

def squareAreas(ml):
    converted = ml * 29.57353
    return None
print(squareAreas(5))

def squareAreas(ml):
    converted = ml * 29.57353
    print(converted)
print("++", squareAreas(5))

def meany(mylist):
   the_meany = sum(mylist)/len(mylist)
   print("in function",the_meany)  
print("meany - ", meany([0,1,2,3]))# como la funcion meany no retorna nada lo impre como None

#En python 
# Procedimiento: No devuelve un valor explícito (aunque en Python devuelve None si no se especifica return).
#Función: Devuelve un valor específico, lo que permite usar el resultado en otras partes del código.
#En Python, todos son técnicamente funciones; la diferencia está en si devuelven un valor explícito o no.

def meanyy(mylist):
    the_meanyy = sum(mylist) / len(mylist)
    return the_meanyy

studentss_gradess = {"Dani":10, "Cesar":8, "Moni":15}
#print(meanyy(studentss_gradess)) mal por que se le esta pasando un diccioanrioo
# 
print(sum(studentss_gradess.values()) / len(studentss_gradess))

#funcion conn conidcionales
def meaniie(value):
    if type(value) == dict:
        the_mean = sum(value.values()) /  len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean        

print("Con condicional = ", meaniie(studentss_gradess))
print("Con condicional = ", meaniie([0,1,2,3,4]))

if True:
    print("Great")
else:
    print("Not greater")    

##
print(isinstance(3, int))# la instancia es de tipo entero

##Operadores Booleanos

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")    
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")

def temp(value):
    if(value > 7):
        num = "Warm"
    else:
         num = "Cold"
    return num

print(temp(10))

def tamStr(value):
    if(len(value)< 8):
        tamanio = False
    else:
        tamanio = True
    return tamanio

print(tamStr("JUANITOSI"))
 
xxi=3
yyi=4

if(xxi>yyi):
    print("x is greater than y")
elif xxi==yyi:
    print("x is equal to y") 
else:
    print("x is less than y")       

def foo(x, array):
    if x in array:
        return True
    else:
        return False
 
print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))


def temp(value):
    if(value > 25):
        num = "Hot"
    elif (value >=15 and value<=25):
         num = "Warm"
    else:
        num = "Cold"
    return num

print(temp(26))

type("abc") == str
type([1, 2, 3]) == list