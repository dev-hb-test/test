import json
from helpers import Helpers
from bs4 import BeautifulSoup
import requests
import random
from datetime import datetime


class Actionner:
    
    def __init__(self):
        self.actions = json.loads(Helpers("actions.json").readFile())
        self.actionner = self.emptyFunction
        # map action names with their functions
        self.functions = {
            "movie_recommendation" : self.movieRecommandation,
            "time_now" : self.timeNow,
            "random_picture" : self.randomPicture,
            "devcrawlers_blog" : self.devcrawlersBlog
        }

    # check if an action must be executed
    def isAction(self, msg):
        # check if its an action
        tokens = msg.split(' ')
        for action in self.actions:
            mesure = 0
            for token in tokens:
                if token in action['keywords'].split(' ') : mesure+=1
            if mesure >= action['max_matches'] : return action['action']
        # if no action executed return false
        return False

    # after running an action, just return the response
    def getResponse(self):
        return self.actionner()

    # handle action if called
    def handle(self, msg):
        action = self.isAction(msg)
        if not action : return False
        # proccess action
        self.actionner = self.functions[action]
        return True

    ############################### Actions Section ##############################
    # initial action
    def emptyFunction(self):
        pass

    # movies recommandation function
    def movieRecommandation(self):
        answers = [
            "I recommend you to watch {}, its a great movie!",
            "Well they say that {} really does the thing",
            "I found this for you : {}",
            "Movies are good, at least you will learn a language, watch this : {}"
        ]
        soup = BeautifulSoup(requests.get("https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512").content, "html.parser")
        movies = soup.find_all('h1', "list-item__title")
        selected_movie = random.choice(movies).text
        return random.choice(answers).format(selected_movie)

    # time function
    def timeNow(self):
        return random.choice([
            "the time now is {}",
            "it's {} now",
            "well, you have your own phone or lap but its {} now"
        ]).format(datetime.now().strftime("%H:%M"))
    
    # return a random picture
    def randomPicture(self):
        return random.choice([
            "Look at this one {}",
            "This one shines {}",
            "I have a lot of picture in my bag, see this one {}"
        ]).format("https://picsum.photos/500/500?random="+str(int(datetime.now().strftime("%M%S"))))

    # get a devcrawlers article
    def devcrawlersBlog(self):
        soup = BeautifulSoup(requests.get("https://devcrawlers.com/en/blog.php").content, "html.parser")
        artile_titles = soup.find_all('a', "d-inline-block")
        random_article = random.choice(artile_titles)
        url = "https://devcrawlers.com/en/"
        return "I found you this : " +random_article.find('h2').text+ ", read more... "+url+random_article['href']

