from time import sleep
q1 = input("How old are you? ")
profile = {}
age = ("age", "Age", "how old am I", "How old am I", "how old am i")


newage = profile['Age'] = q1

print()

q2=input("What's your name? ")

newname = profile['Name'] = q2

print()

q3=input("What's your gender? ")

newgender=profile['Gender'] = q3

print() 

print("THINKING...WAIT A FEW SECONDS")

sleep(2)

print()
print("ALMOST THERE...")
print()
sleep(2)


for i in range(3):
    demand=input("Check what we know about you: ")
    if demand in age:
        
        print()

        print(profile['Age'])

        print()
    else:
        
        print()

        print(profile[demand])

        print() 



print()
print()
sleep(3)
print("Your name is " + profile['Name'] + ", and you're a " + profile["Age"] + " year old " + profile['Gender'])
