
import random

options = ["rock", "paper", "scissors"]
pc_score = 0
user_score = 0

while not (user_score>=5 or pc_score>=5):

    user_input = int(input("What is your choose: 1-rock, 2-paper, 3-scissors\n"))
    user_option = options[user_input-1]
    pc_optin = random.choice(options)
    print(f"user: {user_option}, pc: {pc_optin}")

    if (user_option == options[0] and pc_optin == options[2]) or (user_option == options[1] and pc_optin == options[0]) or (user_option == options[2] and pc_optin == options[1]):
        print(f"user win!")
        user_score += 1
    elif user_option == pc_optin:
        print("Again")
    else:
        print(f"pc win!")
        pc_score += 1
    print(f"user={user_score}, pc={pc_score}")

print("-"*20)

if user_score == 5:
    print(f"Game over! User wins!")
else:
    print(f"Game over! PC wins!")

print("-"*20)




 
