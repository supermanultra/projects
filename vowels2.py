vowels = {'a' : 0,
          'e' : 0,
          'i' : 0,
          'o' : 0,
          'u' : 0 }

word = input("Pick a word to see vowel count: ")
print()

for letter in word:
    if letter in vowels:
        vowels[letter] += 1
for key, value in sorted(vowels.items()):
    if value > 0:
        print(key, 'was found', value, 'time(s)')
        
        
