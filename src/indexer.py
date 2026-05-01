"""
Requirements
1. Called by crawler --> input parameters of (URL, words)
2. Using a for loop we go through this list of words. To obtain the positon of a word we can use the enumerate(Words) - to get position of word.
3. Return back to Crawler.py and prepare to go through another list of words when called again.
4. After all the pages have been scraped and the save function is called, it is then written to a .json file.
    Example of json file <-- AI suggestion to improve my storing of data. 
    {
        "apple": {
            "website/page1": [12, 45, 102, 150, 201],
            "website/page5": [5, 18, 50, 88, 112]
        }
    }

    It is setup like this to allow for quick resolution of the word to the page and position.
    First we look for the word which leads to the webiste page and the positions of the word within the page.
    If this was done the other way around, looking at page first then the word, we would have to look at all the pages which is very time consuming.

5. Function to perform the loading of the json file --> reading of the json file after the load function is called in main.py
    a. Reading of file --> json.load
    b. Store to an object that is used to initialize the search object
"""

import json

class Indexer:
    def __init__(self, index_file='index.json'):
        self.index_file = index_file
        self.index = {}

    def add_words(self, url, words):
        """Adds a list of words and their positions to the index for a specific URL."""
        for position, word in enumerate(words):
            if word not in self.index:
                self.index[word] = {}
            if url not in self.index[word]:
                self.index[word][url] = []
            self.index[word][url].append(position)

    def save(self):
        """Serializes the index dictionary to a JSON file."""
        with open(self.index_file, 'w', encoding='utf-8') as f:
            json.dump(self.index, f)

    def load(self):
        """Loads the index dictionary from a JSON file."""
        try:
            with open(self.index_file, 'r', encoding='utf-8') as f:
                self.index = json.load(f)
            return True
        except FileNotFoundError:
            return False