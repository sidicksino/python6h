customer = {
    "name" : "Nariman",
    "age" : 30,
    "is_student" : True
}
# To get the name in the dictionnary
print(customer.get("name"))
# To update age to 20 
customer["age"] = 20
print(customer.get("age"))


# 
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}

output = ''
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)



# 
message = input(">")
words = message.split(" ")
emojie = {
    ":)": "😆",
    "(:": "🥰",
}

output = ''
for word in words:
    output += emojie.get(word, word) + " "
print(output)