from newsapi import NewsApiClient
import re

api = NewsApiClient(api_key='2ebe588a21f646fd96cae88c16df4c32')

numTitles = 0

pageCount = 1

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

with open('input.txt', 'a') as file:
    while numTitles < 100: # adjust for number of headlines
        all_articles = api.get_everything(q='trump', page=pageCount, pageSize=100)
        articles = all_articles['articles']

        for article in articles:
            if findWholeWord('trump')(article['title']) != None:
                file.write('%s\n' % article['title'])
                numTitles += 1

        pageCount += 1
