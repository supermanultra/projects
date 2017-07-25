phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4): #Don't pa
    plist.pop()
plist.pop(0) #on't pa
plist.remove("'") #ont pa

plist.extend([plist.pop(4)]) #ont ap

plist.insert(2, plist.pop(3)) #on tap


new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

        

