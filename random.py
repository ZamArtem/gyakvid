import random
while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock,paper or scissors?: ").lower()
    if player == computer:
        print("player: ",player)
        print("computer: ",computer)
        print("Tie!")
#------------------------------------------------
    elif player == "rock":
        if computer == "paper":
            print("player: ",player)
            print("computer: ",computer)
            print("You lost!")
        if computer == "scissors":
            print("player: ",player)
            print("computer: ",computer)
            print("You won!")
#-------------------------------------------------
    elif player == "scissors":
        if computer == "rock":
            print("player: ",player)
            print("computer: ",computer)
            print("You lost!")
        if computer == "paper":
            print("player: ",player)
            print("computer: ",computer)
            print("You won!")    
#------------------------------------------------
    elif player == "paper":
        if computer == "scissors":
            print("player: ",player)
            print("computer: ",computer)
            print("You lost!")
        if computer == "rock":
            print("player: ",player)
            print("computer: ",computer)
            print("You won!")  

    play_again = input("Play again (y/n): ").lower()

    if play_again != "y":
        break
print("bye")
