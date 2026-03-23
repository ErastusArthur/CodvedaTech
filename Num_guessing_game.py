import random

def number_guessing_game():
    number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    guess_history = []


    print("Welcome to the Best Number Guessing Game!")
    print(f"""
    I'm thinking of a number between 1 and 100.
    You have {max_attempts} attempts to guess the number.\n""")

    while attempts < max_attempts:

        if guess_history:
            print(f"Previous guesses: {', '.join(map(str, guess_history))}")

        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}\nGuess a number between 1 and 100: "))
        except ValueError:
            print("That's not a valid input. Try again with a whole number.")
            continue

        attempts += 1
        guess_history.append(guess)

        if guess < number:
            print("Your guess is too low...\n")
        elif guess > number:
            print("Your guess is too high...\n")
        else:
            print(f"AMAZINGGGG!!! You got it in {attempts} attempt(s)!\n")
            return

    print(f"GAME OVER! The number was {number}.")
    print("Thank you for playing!")

while True:
    number_guessing_game()
    again = input("Play again? (yes/no): ").strip().lower()
    if again != "yes":
        print(f"Thank you for your time. Goodbye!")
        break