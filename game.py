# game.py

import os
import random

from dotenv import load_dotenv

# setting environment vars: 

load_dotenv()

#
# setting up more things 
# player customization 
#

USER_NAME = os.getenv("USER_NAME", default="Player One")

print("-------------------")
print("Welcome to my Rock-Paper-Scissors game!")
print(f"PLAYER: '{USER_NAME}'")
print("-------------------")

#
# asking user for input
#

user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")


print("You chose:",user_choice)

options = ['rock','paper','scissors']

#
# validate the user selection 
# stop the program (not try to determine the winner)
# if the user choice is invalid 
#

if user_choice in options:
   # print("Good")
   pass
else:
    print("Oops, please choose a valid option and try again!")
    exit()


#
#simulating a computer input
#

computer_choice = random.choice(options)


print("The computer chose:",computer_choice)

#
#determining who won 
#

if user_choice==computer_choice: 
    print("It's a tie!")
elif user_choice=="rock" and computer_choice=="paper":
    print("Oh! The computer won, that's ok!")
elif user_choice=="paper" and computer_choice=="scissors":
    print("Oh! The computer won, that's ok!")
elif user_choice=="scissors" and computer_choice=="rock":
    print("Oh! The computer won, that's ok!")
elif user_choice=="rock"and computer_choice=="scissors":
    print("You win! Congrats!")
elif user_choice=="paper" and computer_choice=="rock":
    print("You win! Congrats!")
elif user_choice=="scissors" and computer_choice=="paper":
    print("You win! Congrats!")

else: 
    print("Oops, something went wrong!")


print("-------------------")


print("Thanks for playing. Let's play again!")


exit ()
