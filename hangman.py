from random import choice
words = ['hangman', 'alien', 'never', 'weed', 'nigger','reverse','zero',
         'nerd','gay','loser','teenager','faggot','propose','weird',
         'python','dunkirk','predator','quick','write','code','stack',
         'counter','hung','arrow','staple','battery','correct','horse']
selection = choice(words)
ns = list(selection)
found = []
for i in range(len(selection)):
    found.insert(0,'_')
hangman = True
guesses = 10
guessed=[]
print("The word is " + str(len(selection)) + " letters long, and you have ten guesses")

while hangman and guesses !=0:
    number = 0
    print()
    if guesses != 10:
        print(str(guesses) + ' guesses left.')
        print()
    guess = input("Guess either a single letter or the whole word: ")
    if len(guess) == 1:
        if guess in ns:
            for letter in ns:
                if guess == letter:
                    found[number] = guess
                    joined = (' '.join(found))
                number += 1
            if guess in guessed:
                print()
                print("You already found that one!")
                print(joined)
            elif ns.count(guess) == 1:
                print()
                print("Nice guess, it's there!")
                print(joined)
            elif ns.count(guess) > 1:
                print()
                print("Wow, it's there more than once! Great!")
                print(joined)
            guessed.insert(0,guess)
        elif guess in guessed:
            print()
            print("You tried that one already, it ain't here! ")
            print(' '.join(found))
        else:
            guessed.insert(0,guess)
            print()
            print("It isn't here!")
            print(' '.join(found))
    else:
        if guess == selection:
            print()
            print("You got it, wow! The word was '" + guess+"'.")
            hangman = False
            guesses = 100
            
        else:
            print()
            print("That's not the word, oops!")
    if found == ns:
        print("Nailed it, '" + selection + "' was the word!")
        hangman = False
        guesses = 100
    
    
    guesses -= 1
    if guesses == 0:
        print()
        print("You ran out of guesses...you lose mate. It was '" + selection + "'.")
    
