import random

options = ("Rock","Paper","Scissor")
game_run = True

while game_run:
    player = None                              # Starting Player is not in options and hence while loop runs 
    while player not in options:
        player=input("Enter a choice (Rock,Paper,Scissor): ")

    computer=random.choice(options)


    print(f"Player: {player}")                  # "f" used for modified and updating values in string like templates
    print(f"Computer: {computer}")

    if player==computer:
        print("It's a tie!")
    elif player=="Rock" and computer=="Scissor":
        print("You win!")
    elif player=="Paper" and computer=="Rock":
        print("You win!")    
    elif player=="Scissor" and computer=="Paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (yes/no): ").lower()
    if not play_again == "yes":
        game_run = False


print("Thanks for playing!")