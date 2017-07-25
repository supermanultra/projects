from bs4 import BeautifulSoup
import requests

url = input('Give a url to parse: ')
r= requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
listofshit=[]
searchwords =input("Give a word to look for: ")
for link in soup.find_all('a'):
    listofshit.append(link.get('href'))
newlos=list(s and s.replace('/','') for s in listofshit)
newlos=list(s and s.replace('-',' ') for s in newlos)
        
number = 0

for item in newlos:
    if newlos[number]:
        if searchwords in newlos[number]:
            print(searchwords + " : " + item)
    number += 1
        
    
