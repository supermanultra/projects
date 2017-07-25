run = True
from random import randint

while run == True:
    roll = randint(1,6)
    print("The dice rolls and it's a " + str(roll))
    print()
    k = input("Wanna roll again? ")
    print()
    if k == 'no':
        run = False
        print("Bye!")
    
