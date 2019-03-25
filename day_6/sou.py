from bs4 import BeautifulSoup
import requests


def beautiful_soup():

    wordCount = 0

    pageCount = 0

    wordLimit = True

    with open('input.txt', 'w') as file:

        with requests.Session() as session:

            while wordLimit:

                response = session.get("https://greensdictofslang.com/browse/?page=%s" % pageCount)
                soup = BeautifulSoup(response.text, "lxml")

                list = soup.find('ul', {'class': "browselist"})

                for word in list.find_all('li'):
                    if wordCount < 10: # adjust for number of headlines
                        unsplitWord = word.text
                        splitWord = unsplitWord.split(',')[0]
                        print(splitWord)
                        # file.write('%s\n' % quote.text)
                        wordCount += 1
                        continue
                    else:
                        wordLimit = False
                        break

                pageCount += 1

beautiful_soup()
