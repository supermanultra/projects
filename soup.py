from bs4 import BeautifulSoup
import requests

url = 'http://www.pythonforbeginners.com/'
r= requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
listofshit=[]
searchwords = ['continue', 'quick guide', 'web']
for link in soup.find_all('a'):
    listofshit.append(link.get('href'))
newlos=list(s.replace('/','') for s in listofshit)
newlos=list(s.replace('-',' ') for s in newlos)
        
number = 0

for item in newlos:
    for word in searchwords:
        if word in newlos[number]:
            print(word + " : " + item)
    number += 1
        
    
