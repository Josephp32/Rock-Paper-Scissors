import random

while True:
    user_move = input("Enter a choice (rock, paper, scissors): ")
    possible_moves = ["rock", "paper", "scissors"]
    computer_move = random.choice(possible_moves)
    print(f"\nYou chose {user_move}, computer chose {computer_move}.\n")

    if user_move == computer_move:
        print(f"Both players selected {user_move}. It's a tie!")
    elif user_move == "rock":
        if computer_move == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_move == "paper":
        if computer_move == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_move == "scissors":
        if computer_move == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Would you like to continue playing? Enter 'y' for yes and 'n' for no. ")
    if play_again.lower() != "y":
        break
    