import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)  

    while player not in options:
        player = input("enter a choice (rock,paper,scissors): ")

    print(f"player : {player}")
    print(f"computer : {computer}")

    if computer == player:
        print("it's a tie! ")
    elif player == "rock" and computer == "paper":
        print("you lose")  
    elif player == "paper" and computer == "rock":
        print("you win")  
    elif player == "scissors" and computer == "paper":
        print("you win")
    elif player == "scissors" and computer == "rock":
        print("you lose")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer == "scissors":
        print("you lose")

    play_again = input("do you want to play again? (y/n): ").lower()
    if not play_again == "y":
        running = False

print("thanks for playing!")
