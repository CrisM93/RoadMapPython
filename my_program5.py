
word_input = ''
word_say = ''
#for comment use ctrl +k ctrl +c
#for uncomment use ctrl +k ctrl +u


# while True:
#     word_input = input("Say something ")

#     if word_input =="\end":
#         print(word_say)
#         break
#     else:
#         final_word =word_input[0].upper() + word_input[1:].lower()+ "."
#         word_say = word_say + " " + final_word
#         continue


def sentence_maker(phrase):
    interrogatives = ("how", "what", "why", "where", "when", "who")
    capitalized = phrase.capitalize()# Capitalizes the first letter of the phrase
    if phrase.startswith(interrogatives):#for checking if the phrase starts with any of the interrogatives
        return "{}?".format(capitalized)#puts a question mark at the end of the phrase
    else: 
        return "{}.".format(capitalized)#puts a period at the end of the phrase

results = []
while True:
    user_input = input("Say something:")
    if user_input == "\end":
        print("Goodbye!")
        break
    else:
        results.append(sentence_maker(user_input))
        continue
print(" ".join(results))#another way to join the list of results into a single string