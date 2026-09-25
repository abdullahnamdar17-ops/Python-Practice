import random

choices = {1 : "Snake", 2 : "Water", 3 : "Gun"}
beats = {
    "Snake": "Water",
    "Water": "Gun",
    "Gun": "Snake"
}

print ("Welcome to Snake, Water and Gun Game!")

while True:
    print("Choose your option: \n1. Snake \n2. Water \n3. Gun \n4. Exit" )
    user_input = int((input("Enter your choice (1/2/3/4): ")))

    if user_input == 4:
        print("Exiting the game. Goodbye")
        break
        
    if user_input not in choices:
        print("Invalid choice. Please try again.")
        continue

    user_choice = choices[user_input]
    computer_choice = random.choice(list(choices.values()))
    # print(f"Computer choose: {computer_choice}")

    if user_choice == computer_choice:
        print(f"Both chose {user_choice}. It's a tie!")

    elif beats[user_choice] == computer_choice:
        print(f"You chose {user_choice} and computer chose {computer_choice}. 'You win!'")
