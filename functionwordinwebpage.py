def wordInWebPage(url: str, word: str) -> bool:
    """Takes a URL and keyword, checks if the word is found on the webpage and
        returns a boolean. Stores finds inside dictionary within function
        called 'wordandphrase'"""
    from bs4 import BeautifulSoup
    import requests
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    listofshit = []
    number = 0
    wordandphrase = {}
    for link in soup.find_all('a'):
        listofshit.append(link.get('href'))
    newlos = list(s and s.replace('/', '') for s in listofshit)
    newlos = list(s and s.replace('-', ' ') for s in newlos)
    for item in newlos:
        if newlos[number]:
            if word in newlos[number]:
                wordandphrase[word + str(number)] = item
        number += 1
    if bool(wordandphrase):
        return True
    else:
        return False
