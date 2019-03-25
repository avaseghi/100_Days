from bs4 import BeautifulSoup
import requests


def beautiful_soup():

    with open('input.txt', 'w') as file:

        request = requests.get("http://www.historyplace.com/speeches/previous.htm")
        previousSoup = BeautifulSoup(request.text, "lxml")

        unorderedList = previousSoup.find('ul')

        totalLinks = 1

        for links in unorderedList.find_all('li'):
            file.write("%s. %s" %(totalLinks, links.a.text))
            totalLinks += 1
            speechLink = links.a.get('href')

            file.write('\n')

            with requests.Session() as session:

                response = session.get("http://www.historyplace.com/speeches/%s" % speechLink)
                soup = BeautifulSoup(response.text, "lxml")

                textBlock = soup.find('blockquote')

                while len(textBlock.select('b')) == 0 and len(textBlock.select('strong')) == 0:
                    textBlock = textBlock.find_next_sibling('blockquote')

                # file.write(textBlock.text)
                for text in textBlock.stripped_strings:
                    file.write('%s\n' % text)

            file.write('\n')

        print(totalLinks)

beautiful_soup()
