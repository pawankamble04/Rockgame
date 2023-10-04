import random

# Initialize scores
user_score = 0
computer_score = 0

while True:
    # User input
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    # Validate user input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    
    # Generate computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    
    # Display choices and result
    print(f"You chose {user_choice}, computer chose {computer_choice}. {result}")
    print(f"Your score: {user_score}, Computer's score: {computer_score}")
    
    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")
