import random

initial = 1
final = 10
restart = {"yes", "y", "ok"}
max_attempts = 3

while True:
    wins = 0
    rounds = 0
    print("\nNew Game Started! Guess the number between", initial, "and", final)

    while rounds < max_attempts:
        rounds += 1
        print(f"\nRound {rounds} of {max_attempts}")
        user_input = int(input("Enter your guess: "))
        pc_generated_integer = random.randint(initial, final)
        print("PC's number:", pc_generated_integer)

        if user_input > pc_generated_integer:
            print("Too high!")
        elif user_input < pc_generated_integer:
            print("Too low!")
        else:
            print("You guessed it right!")
            wins += 1

    if wins > 0:
        print("\n YOU ARE A WINNER!")
    else:
        print("\nYOU LOST! Better luck next time!")

    user_input = input("Want to play again? (yes/y/ok to restart): ").lower()
    if user_input not in restart:
        print("Thanks for playing! Goodbye!")
        break
