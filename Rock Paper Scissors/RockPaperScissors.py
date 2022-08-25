import random #always have your imports a the top
#2 creating 2 variables one for the user ad one for the computer

UserWins = 0
Computer_wins = 0

options = ["rock", "paper", "scissors"]
#options =    0,      1,       2

while True:
    user_input = input("Choose Rock Paper or scissors or press Q to Quit: ").lower()
    if user_input == "q":
        break
       
    #now inputting various inputs instead of one thing using multiple if statements outputting str's
    #use a lst
    if user_input not in options: #checking if user input is not within the specified list
        continue

    #if user has inputed valid input now computer will generate a random number
    random_number = random.randint(0, 2)
    C_Picks = options[random_number] #Computer chooses either options via random number
    print("Computer has chosen: ", C_Picks)

    #now comparing who won between user and computer. IF statement 
    if user_input == "rock" and C_Picks == "scissors": #and condition checks whether both conditions are true in if. Or is opposite as it checks if either are true
        
        print("You Won!!")
        UserWins += 1
        
    
    elif user_input == "paper" and C_Picks == "rock": 
        
        print("You Won!!")
        UserWins += 1
        
    
    elif user_input == "scissors" and C_Picks == "paper": 
        
        print("You Won!!")
        UserWins += 1
    
    else:
        print("You Just Lost Sorry!!")
        Computer_wins += 1

print("You have won", UserWins, "times")
print("The computer won", Computer_wins, "times")

print("Goodbye!!")