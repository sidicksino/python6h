age = int(input("Age :"))
income = 20000
risk = income / age
print(age)

# Here if user input a string value the error will be "ValueError"
# and if user input age to 0 the error will be "ZeroDivisionError" we can divide a number by Zero
# To solve this we need to use try except in python

try:
    age = int(input("Age :"))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Age must be a number")
except ZeroDivisionError:
    print("We can divide a number by Zero")