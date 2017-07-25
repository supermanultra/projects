from random import randint
from time import sleep
awins = 0
bwins = 0

while awins < 3 and bwins < 3:

    computerchoice = input("Player A: Rock, paper, scissors? ")

    print("\n" * 100)

    userchoice = input("Player B: Rock, paper, scissors? ")

    print()
    print("Player A chooses", computerchoice)
    print()
    print("Player B chooses", userchoice)
    print()
    sleep(2)
    print("\n" * 100)

    if computerchoice == userchoice:
        print("Tie!")

    if computerchoice == 'paper': 
        if userchoice == "rock":
            print("Player A wins, paper beats rock!")
            awins += 1
        if userchoice == "scissors":
            print("Player B wins, scissors beats paper!")
            bwins += 1


    if computerchoice == 'rock':
        if userchoice == 'paper':
            print("Player B wins, paper beats rock!")
            bwins += 1
        if userchoice == 'scissors':
            print("Player A wins, rock beats scissors!")
            awins += 1


    if computerchoice == 'scissors':
        if userchoice == 'paper':
            print("Player A wins, scissors beats paper!")
            awins += 1
        if userchoice == "rock":
            print("Player B wins, rock beats scissors!")
            bwins +=1

    print()
    print("\n", "Player A wins: ", awins, "\n", "Player B wins: ",  bwins)
    sleep(3)
    print("\n" * 100)

if awins == 3:
        print("Player A has won three games and takes the crown!")

if bwins == 3:
    print("Player B has won three games and takes the crown!")











