import random


def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # You can change this if you want more/less tries

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("⛔ Please enter a valid number!")
            continue

        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try a higher number.")
        elif guess > secret_number:
            print("📈 Too high! Try a lower number.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempt(s)!")
            break
    else:
        print(f"💀 Game over! The correct number was {secret_number}.")


# Run the game
number_guessing_game()
