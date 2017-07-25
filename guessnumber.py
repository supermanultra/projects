from random import randint
run = True
while run:
    computer = randint(1,5)
    lists = [1,2,3,4,5]
    user = input("Pick a number from 1 to 5! ")
    print()
    if int(user) == computer:
        print("You got it! The computer also chose " + str(user))
    elif int(user) not in lists:
        print("You picked a number outside of the range")
    else:
        print("You picked the wrong number, it was " + str(computer))
    print()
    q = input("Wanna try again? ")
    print()
    if q == "no":
        run = False
        print("Bye!")
    print()
