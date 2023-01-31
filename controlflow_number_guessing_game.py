import random
random_number_game = random.randint(1, 20)

print("guess a number between 1 and 20")
for num in range(3):
    user_guess = int(input())
    if user_guess == random_number_game:
        print("You guessed right")
        break
    elif user_guess > random_number_game:
        print("You guessed to high, guess lower")
    elif user_guess < random_number_game:
        print("You guessed to low, guess higher")
else:
    print(f"You didn't guess correct in three tries. The answer was {random_number_game}")