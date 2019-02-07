from bs4 import BeautifulSoup
import requests


def beautiful_soup():

    quoteCount = 0

    pageCount = 1

    with open('input.txt', 'w') as file:

        with requests.Session() as session:

            while quoteCount < 10: # adjust for number of headlines
                response = session.get("https://quotecatalog.com/quotes/deep/page/%s" % pageCount)
                soup = BeautifulSoup(response.text, "lxml")

                for quote in soup.find_all('a', {'class': 'quote__text'}):
                    # print(quote.text)
                    file.write('%s\n' % quote.text)
                    quoteCount += 1

                pageCount += 1

beautiful_soup()
