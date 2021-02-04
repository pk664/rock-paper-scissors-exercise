# game.py


import random
print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#
#asking user for input
#

user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")


print("You chose:",user_choice)



#
#simulating a computer input
#




options = ['rock','paper','scissors']

computer_choice = random.choice(options)


print("The computer chose",computer_choice)


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


print("Thanks for playing. Please play again!")


exit ()
