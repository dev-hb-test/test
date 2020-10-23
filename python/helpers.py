import os

class Helpers:

    def __init__(self, filename):
        self.filename = filename
    
    # reads a specific file with given filename
    def readFile(self):
        content = ""
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.filename)) as f:
            for line in f.readlines():
                content += line
        return content