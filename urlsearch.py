from bs4 import BeautifulSoup
import requests


def urlsearch(url:str, keyword:str) -> str:
    key = []
    key.append(keyword)
    r  = requests.get("http://" +url)
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        if link in key:
            print(link.get('href'))
        else:
            print('None found')
