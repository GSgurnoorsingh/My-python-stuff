#This whole concept used in this code is interaction between functions

from random import shuffle

randomlist=['','','O'] #Creates a list with the ball in it

def randomfunction(randomlist): #A Function that shuffles the list above and returns its value
    shuffle(randomlist)
    
    return randomlist

def player_guess(): #This function will store player's guess 
    
    playerguess=""
    
    while playerguess not in ['0','1','2']:
       playerguess=input("Enter your guess (0,1,2) : ")
       
    return int(playerguess)
       

def check_guess(randomlist,playerguess): #For checking the guess we combined the list and player_guess function
    if randomlist[playerguess]=='O':
        print("You guessed right")
    else:
        print("You guessed wrong")
        print(f"The correct one is \n {randomlist}")
        
mixed_up_list=randomfunction(randomlist)
playerguess=player_guess()

check_guess(mixed_up_list,playerguess) #Then finally we called the function and produced the desired output