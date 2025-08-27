# temps = [210, 234, 340, 230]

# new_temps =[]
# for temp in temps:
#     new_temps.append(temp/10)#adding each temperature divided by 10 to new_temps
# print(new_temps)

temps = [221, 234, 340, -9999, 230]

new_temps = [temp/10 for temp in temps if temp != -9999 ]
print(new_temps)

def only_Numerics(values):
    if(values.__class__ == list):
        return [value for value in values if isinstance(value, int)]
    else:
        return "Input is not a list"  
    
print(only_Numerics([1, 'a', 2, 'b', 3, 'c']))

# def only_positive_numbers(values):
#     if(values.__class__ == list):
#         return [value for value in values if value > 0]
#     else:
#         return "Input is not a list"
    
# print(only_positive_numbers([1, -2, 3, -4, 5, -6]))

new_temps =[temp/10 if temp != -9999 else 0 for temp in temps]
print(new_temps)

def only_Numerics(values):
    if(values.__class__ == list):
        return [value if isinstance(value, int) else 0 for value in values]
    else:
        return "Input is not a list"

print(only_Numerics([1, 'a', 2, 'b', 3, 'c']))

def sum_list_except_string(values):
    # print(values.__class__) #prints the class type of values
    # print(isinstance(values, list))#prtints if values is an instance of int, float etc
    # print(type(values))#prints the type of values in this case list
    total = 0
    if(values.__class__ == list):
        for value in values:
            if isinstance(value, float):
                total = total + value
            else:
                try:#here we try to convert value to float
                    aux = float(value)#here we try to convert value to float
                    total = total + aux
                except:#here if it fails we just
                    continue#skip to the next iteration
        return total
    else:
        return total
    
print(sum_list_except_string(['1.2', '2.6', '3.3', "ABA"]))   

# def sum_list_except_string(values):
#     total = 0.0
#     if isinstance(values, list):
#         for value in values:
#             try:
#                 total += float(value)  # intenta convertir cualquier cosa
#             except (ValueError, TypeError):
#                 continue  # si no se puede, lo ignora
#     return total




