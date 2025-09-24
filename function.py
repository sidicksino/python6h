# function
def greet_user():
    print('Hi there !')
    print('Welcome to your sino boutique !')


print("Start")
greet_user()
print("finiched")




# add parameter to a function
def greet_user(name):
    print(f'Hi {name} !')
    print('Welcome to your sino boutique !')


print("Start")
greet_user("sidick")
print("finiched")




# add multiple parameter to a function
def greet_user(firdt_name, last_name):
    print(f'Hi {firdt_name} {last_name} !')
    print('Welcome to your sino boutique !')


print("Start")
greet_user("Sidick", "Abdoulaye")
print("finiched")




# keyword argument
def greet_user(firdt_name, last_name):
    print(f'Hi {firdt_name} {last_name} !')
    print('Welcome to your sino boutique !')


print("Start")
greet_user(last_name="Abdoulaye", firdt_name="Sidick")
print("finiched")




# return statement
def square(number):
    return number * number


print(square(3))




# 
def message_user(message):
    words = message.split(" ")
    emojie = {
        ":)": "😆",
        "(:": "🥰",
    }
    output = ''
    for word in words:
        output += emojie.get(word, word) + " "
    return output


message = input(">")
print(message_user(message))
