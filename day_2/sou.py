from bs4 import BeautifulSoup
import requests
import json
import re

def beautiful_soup():

    startTime = "/"

    headlineCount = 0

    with open('input.txt', 'w') as file:

        with requests.Session() as session:

            while headlineCount < 1000: # adjust for number of headlines
                response = session.get("https://www.theonion.com%s" % startTime)
                soup = BeautifulSoup(response.text, "lxml")

                for article in soup.find_all('article'):
                    category = article.find(text = re.compile('News'))
                    if category != None:
                        header = article.header.h1.a.text
                        file.write('%s\n' % header)
                        headlineCount += 1

                button = soup.find('div', {'class': 'load-more__button'})
                startTime = button.a.get('href')

beautiful_soup()
