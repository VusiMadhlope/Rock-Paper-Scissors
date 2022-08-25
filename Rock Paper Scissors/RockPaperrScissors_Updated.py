import random
from secrets import choice
User_Wins = 0
computer_wins = 0
Score = 0
Tie = 0

Choices = ["Rock", "Paper", "Scissors"]

while True:
    UserDecision = input("Please type in your selected choice or type Q to Quit: ")
    if UserDecision == "Q":
        break

    if UserDecision not in Choices:
        print("Choose Only The Options please")
        continue

    R_Number = random.randint(0, 2)
    Computer_picks = Choices[R_Number]
    print("The computer has chosen: ", Computer_picks)
 
    if UserDecision == "Rock" and Computer_picks == "Scissors":
        print("you have won congrats!!!")
        User_Wins += 1
    
    elif UserDecision == "Paper" and Computer_picks == "Rock":
        print("you have won congrats!!!")
        User_Wins += 1
    
    elif UserDecision == "Scissors" and Computer_picks == "Paper":
        print("you have won congrats!!!")
        User_Wins += 1
    
    ##############################
    #Now if their is a tie
    elif UserDecision == "Rock" and Computer_picks == "Rock":
        print("Their was a tie go again!!")
        Tie == 0

    
    elif UserDecision == "Paper" and Computer_picks == "Paper":
         print("Their was a tie go again!!")
         Tie == 0
    
    elif UserDecision == "Scissors" and Computer_picks == "Scissors":
        print("Their was a tie go again!!")
        Tie == 0
    
    else:
        print("You just lost to the computer sorry!!")
        computer_wins += 1

print("You won", User_Wins, "times. NICE")
print("The computer won", computer_wins, "times")

print("GOOODBYYYYEEEEE!!!!!")
        