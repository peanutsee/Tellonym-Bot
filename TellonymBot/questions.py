'''
This scrapper is specific to https://www.teenvogue.com/story/20-questions-ask-best-friend-become-closer-relationships
Sibei heng ah this one is not headless website... or else taotia already
'''

from bs4 import BeautifulSoup as bs
import requests
import re

class QuestionsScraper():
    def questions(self):
        url = 'https://www.teenvogue.com/story/20-questions-ask-best-friend-become-closer-relationships'
        page = requests.get(url)
        soup = bs(page.content, 'html.parser')
        questions = soup.find('div', {'class' : 'grid--item body body__container article__body grid-layout__content'}).find_all('h2')
        questionsRendered = [re.sub('<h2>|</h2>','', str(i))[3:] for i in questions]
        return questionsRendered