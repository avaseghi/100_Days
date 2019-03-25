from bs4 import BeautifulSoup
import requests


def beautiful_soup():

    creatureNum = 0

    creatureLimit = True

    with open('input.txt', 'w') as file:

        with requests.Session() as session:

            for x in range(65,90):

                while creatureLimit:

                    response = session.get("https://en.wikipedia.org/wiki/List_of_legendary_creatures_(%s)" % chr(x))
                    soup = BeautifulSoup(response.text, "lxml")

                    list = soup.find('ul')

                    for creature in list.find_all('li'):
                        if creatureNum < 10: # adjust for number of headlines
                            unsplitWord = creature.text
                            splitWord = unsplitWord.split('(')[0]
                            print(splitWord)
                            # file.write('%s\n' % quote.text)
                            creatureNum += 1
                            continue
                        else:
                            creatureLimit = False
                            break

beautiful_soup()
