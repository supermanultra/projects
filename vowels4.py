vowels = set("aeiou")

word = input("Pick a word to see vowels: ")

i = vowels.intersection(set(word))

for l in i:
    print(l)
