#Pawan_Singh_a
from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False
while player == False:
    player = input("Rock, Paper, Scissors?    -- ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play.Something error in your input found!")
    #player was set to True, but we want it to be False so the loop continues here
    player = False
    computer = t[randint(0,2)]
    
    
    
    
    

    
    
# a=input("user input:   ")
# b=list(a)
# index=int(input("index:  "))
# a[index]==4
# print(b)
