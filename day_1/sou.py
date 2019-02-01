from bs4 import BeautifulSoup
import requests
import string

categories = ["quizzes","quizzes-can-we-guess", "quizzes-disney", "quizzes-food", "quizzes-personality", "quizzes-would-you-rather", "quizzes-love", "quizzes-trivia"]

def beautiful_soup():

    with open('input.txt', 'w') as file:

        originalCount = 0

        for category in categories:

            with requests.Session() as session:

                for page in range(1, 10):
                    response = session.get("https://www.buzzfeed.com/us/feedpage/feed/%s?page=%s&page_name=quizzes&" % (category, page))
                    soup = BeautifulSoup(response.text, "lxml")
                    for headline in soup.find_all('h2'):
                        textOnly = headline.text
                        if textOnly != "We can't find the page you're looking for.":
                            unpunctuated = textOnly.translate(str.maketrans('','', string.punctuation))
                            file.write('%s\n' % unpunctuated)
                            originalCount += 1

    print("Orinigal number of headlines %s" %originalCount)

    file.close()

    headlines = None

    with open('input.txt', 'r') as file:

        headlines = set(file.readlines())

    file.close()

    with open('input.txt', 'w') as file:
        newCount = 0

        for uniqueHeadline in headlines:
            file.write(uniqueHeadline)
            newCount += 1
            
        print("Unique number of headlines %s" %newCount)

    file.close()

beautiful_soup()
