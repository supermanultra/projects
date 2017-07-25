vowels = ["a", "e", "i", "o", "u"]
word = input("Write a word with vowels in it: ")
found = []
for i in word:
    if i in vowels:
        if i not in found:
            found.append(i)
for vowel in found: 
    print(vowel)



