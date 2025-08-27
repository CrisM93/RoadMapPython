# myfile = open("fruits.txt")#here we open the file
# content = myfile.read()#here we read the content of the file
# # print(myfile.read())#here we read the file
# print(content)#here we print the content of the file
# myfile.close()#here we close the file
# print(content)

# with open("ejemplo/fruits.txt") as myfile:#here we open the file
#     content = myfile.read()#here we read the content of the file
# print(content)#here we print the content of the file
# #here we close the file automatically

# with open("ejemplo/fruits.txt", "w") as myfile:#here we open the file in read mode
#      myfile.write("Tomato\nCucumber\nOnion")#here we read the content of the file
#      myfile.write("\nPotato")#here we read the content of the file
#      myfile.write("\nCarrot")#here we read the content of the file


# with open("ejemplo/fruits.txt") as myfile:# Read the bear.txt file, and print out the first 90 characters of its content.
#     content = myfile.read(90)#here we read the content of the file
# print(content)#here we print the content of the file

# def number_of_occurrences(myfiles, word):
#     with open(myfiles) as myfile:
#         content = myfile.read()
#         words = content.split()
#         count = 0
#         for w in words:
#             if w.lower() == word.lower():
#                 count += 1
#     return count

# print(number_of_occurrences("ejemplo/fruits.txt", "Tomato"))

# def count_character_in_file(char, filepath):
#     with open(filepath) as f:
#         content = f.read()
#     return content.count(char)

# print(count_character_in_file("a", "ejemplo/fruits.txt"))

# with open("file.txt", "w") as f: #here we open the file in write mode
#     f.write("Sanil!\n")#here we write to the file

#this will append the first 90 characters of fruits.txt to first.txt 
with open("ejemplo/fruits.txt") as f:
    with open("first.txt", "a") as f1: #here "a" means append mode so it will not overwrite the file
        f1.write(f.read(90))
