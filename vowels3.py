vowels = ["a", "e", "i", "o", "u"]

found = {}


word = input("Pick a word to see vowel count: ")

for l in word:
    if l in vowels:
        found.setdefault(l,0)
        found[l] += 1

for k, v in sorted(found.items()):
    print(k, "was found", v, "time(s)")
