from random import randint
from time import sleep
computerchoice = randint(1,3)

if computerchoice == 1:
    computerchoice = "paper"
if computerchoice == 2:
    computerchoice = "rock"
if computerchoice == 3:
    computerchoice = "scissors"



userchoice = input("Rock, paper, scissors? ")

print()
print("Computer chooses", computerchoice)
print()
sleep(2)

if computerchoice == userchoice:
    print("Tie")

if computerchoice == 'paper': 
    if userchoice == "rock":
        print("You lose, paper beats rock!")
    if userchoice == "scissors":
        print("You win, scissors beat paper!")


if computerchoice == 'rock':
    if userchoice == 'paper':
        print("You win, paper beats rock!")
    if userchoice == 'scissors':
        print("You lose, rock beats scissors!")


if computerchoice == 'scissors':
    if userchoice == 'paper':
        print("You lose, scissors beats paper!")
    if userchoice == "rock":
        print("You win, rock beats scissors!")
              

        
