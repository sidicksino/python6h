guess_counts = 0
guess_limit = 3
secret_number = 9

while guess_counts < guess_limit:
    guess = int(input("Guess : "))
    guess_counts += 1
    if guess == secret_number:
        print("You Won!")
        break
else:
    print("Sorry, you failed!")