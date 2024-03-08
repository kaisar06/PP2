def guess_number(number):
    secret_number = 9

    if number > secret_number:
        print("Your guess is too high")
    elif number < secret_number:
        print("Your guess is too low")
    else:
        return True

name = input("Hello! What is your name?")
print("Well,", name, "I am thinking of a number between 1 and 20.")

num = int(input("Take a guess."))
counter_of_guesses = 0

while not guess_number(num):
    counter_of_guesses += 1
    num = int(input("Take a guess."))

print("Good job, ", name, "! You guessed my number in ", counter_of_guesses, " guesses!")
