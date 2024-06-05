import random

choices = ("rock", "paper", "scissors")

while True:
    computer = 0
    player = 0
    
    while computer < 3 and player < 3:
        p1 = ""
        
        while p1 not in choices:
            p1 = input("rock, paper, or scissors? ").lower()
        
        comp = random.choice(choices)
        
        if p1 == comp:
            print("computer:", comp)
            print("player:", p1)
            print("It's a tie!")
        elif p1 == "rock":
            if comp == "paper":
                print("computer:", comp)
                print("player:", p1)
                computer += 1
            else: 
                print("computer:", comp)
                print("player:", p1)
                player += 1
        elif p1 == "paper":
            if comp == "scissors":
                print("computer:", comp)
                print("player:", p1)
                computer += 1
            else:  
                print("computer:", comp)
                print("player:", p1)
                player += 1
        elif p1 == "scissors":
            if comp == "rock":
                print("computer:", comp)
                print("player:", p1)
                computer += 1
            else:  
                print("computer:", comp)
                print("player:", p1)
                player += 1
        
        print("computer score:", computer)
        print("player score:", player)
    
    if computer > player:
        print("You lose!")
    else:
        print("You win!")
    
    con = input("Do you want to play again? yes/no: ").lower()
    if con != "yes":
        break

print("Bye!")
