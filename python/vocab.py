import pandas as pd
import random
import requests
import json
import numpy as np
from helpers import Helpers
import os

class Vocab :

    def __init__(self, v):
        print("Downloading dataset from devcrawlers.com ....")
        self.data_server = json.loads(requests.get("https://devcrawlers.com/discord/hafid/fetch.php?action=getall").content)
        print("Dataset downloaded successfully!")
        self.file_name = v + ".json"
        self.data = json.loads(Helpers(self.file_name).readFile())
        self.skip_words = ['khay', 'khoya', 'khouya', 'db', 'chi', 'xi', '?', 'o', 'ou', 'lah', 'llah', 'ihafdak', 'yhafdak', 'ihfdek', 'yhfdek', 
        'yhfdak', 'hafid', '/hafid']
        self.dirty_words = ['9wad', '9wed', '9wd', 'pute', 'cock'
            ,'zeb', 'zab', 'lker', 'lkar', 'fuck', 'bitch', 'sex', 'tabon', 'zb', 'porn', 'pornhub', 'xnxx', 'brazzerz', 'xxx', 'xlxx', 'xvideo',
                'xvideos', 'bobs', 'nipples', 'bzazl', 'bzazel', 'tboun', 'tbon', 'tabon', 'taboun', '9lawi', '9lwi', 'qlawi', 'klawi', '9lwa']
        print("Hafid has fully initialized!")

    # get response from json file
    def get(self, key, rand = False):
        if not rand : return self.data[key]
        else : return random.choice(self.data[key])

    # get index of maximum
    def getMax(self, lst):
        max = 0
        i = 0
        for t in lst:
            if t >= max :
                max = t
            i += 1
        return max

    def getIndexOfMax(self, lst, max):
        i = 0
        index = []
        for t in lst:
            if t == max :
                index.append(i)
            i += 1
        return index

    # get response from database server
    def process(self, msg):
        # check for dirty words
        for dw in self.dirty_words:
            if dw in msg : return "please respect the members, we don't say that here"
        # process if clean
        confusion_vector = np.zeros(len(self.data_server))
        k = 0
        for v in self.data_server:
            for word in msg.split(' '):
                if word not in self.skip_words :
                    if word in v['question'] : 
                        confusion_vector[k] += 1
            k += 1
        # get indexes with the same maximum
        answer_index = self.getIndexOfMax(confusion_vector, self.getMax(confusion_vector))

        # needs to be upgraded (add length check)
        answer_index = answer_index[0]
        # get single answer
        if confusion_vector[answer_index] == 0 : return "I'm slill learning, help me from here https://devcrawlers.com/discord/hafid/"
        return self.data_server[answer_index]['answer']

