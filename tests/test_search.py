"""
Cases for print and find command
Basic functionality
1. Functionality of print <word>
    a. Given a valid command arg, return appropraite result
    b. Error checking when given 
        i. Missing <Word>
        ii. Given <word1, word2>
        iii. Handing of word inexistance

2. Functionality of find <Word(s)>
    a. Find and show the results when given 1 / 2 word(s) for find command
    b. Error checking
        i. Missing <Words>
        ii. Handing of word inexistance

Edge cases for both
1. Words with apostrophe --> Like Joshua's 
2. Missing word(s)
3. Incorrect number of word(s)
4. Capitalisation of word(s)
"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.indexer import Indexer
from src.search import Searcher

class TestSearcher(unittest.TestCase):
    def setUp(self):
        self.indexer = Indexer()
        # Loading the indexer with fake data
        self.indexer.index = {
            "good": {"url1": [0], "url2": [5]},
            "friends": {"url2": [6], "url3": [10]},
            "nonsense": {"url1": [1, 2, 3, 4, 5, 6]},
            "joshua's": {"url1": [7, 15]} 
        }
        self.searcher = Searcher(self.indexer)


    # print <word> functionality

    @patch('sys.stdout', new_callable=StringIO)
    # Redirects the output from sys.stdout to the StringIO object
    # Essentially to just prevent the test from printing to the terminal. 

    def testPrintWordFrequency(self, mock_stdout):
        # Valid command arg

        self.searcher.printWord("nonsense")
        output = mock_stdout.getvalue()
        # retrieving data from the virtual buffer.
        self.assertIn("6", output) # Checking for frequency
        self.assertIn("1, 2, 3, 4, 5, 6", output) # Checking for positions

    
    # 1b(i). Missing <Word> - Has been dealt with in the main.py so no need to check in search.py

    @patch('sys.stdout', new_callable=StringIO)
    def testPrintTooManyWords(self, mock_stdout):
        # Given <word1, word2>

        self.searcher.printWord("good friends")
        output = mock_stdout.getvalue()
        # Recognize there are two words and return an error
        self.assertIn("error", output.lower())

    @patch('sys.stdout', new_callable=StringIO)
    def testPrintWordNonexistent(self, mock_stdout):
        # Handling of word inexistence

        self.searcher.printWord("aliens")
        output = mock_stdout.getvalue()
        self.assertIn("not found", output.lower())

    

    # find <word(s)> functionality

    @patch('sys.stdout', new_callable=StringIO)
    def testFindSingleWord(self, mock_stdout):
        # Find a word

        self.searcher.find("good")
        output = mock_stdout.getvalue()
        self.assertIn("url1", output)
        self.assertIn("url2", output)
        self.assertNotIn("url3", output)

    @patch('sys.stdout', new_callable=StringIO)
    def testFindMultipleWords(self, mock_stdout):
        # Find 2 words

        # should return url2 as it has both good and friends
        self.searcher.find("good friends")
        output = mock_stdout.getvalue()
        self.assertIn("url2", output)
        self.assertNotIn("url1", output)
        self.assertNotIn("url3", output)

    # 2b(i) Missing <Words> - Also has been dealt with in main.py so there is no need to check

    @patch('sys.stdout', new_callable=StringIO)
    def testFindNoResults(self, mock_stdout):
        # Handling of word inexistence

        self.searcher.find("aliens")
        output = mock_stdout.getvalue()
        self.assertIn("no pages found", output.lower())

    @patch('sys.stdout', new_callable=StringIO)
    def testFindPartialInexistence(self, mock_stdout):
        # Handling of word inexistence where one word exist and the other doesn't

        # 'good' exists, but 'aliens' doesn't. Expect to return no pages found.
        self.searcher.find("good aliens")
        output = mock_stdout.getvalue()
        self.assertIn("no pages found", output.lower())


    # Edge cases for both commands


    @patch('sys.stdout', new_callable=StringIO)
    def testApostropheHandlingFind(self, mock_stdout):
        # Words with apostrophe for find

        self.searcher.find("joshua's")
        output = mock_stdout.getvalue()
        self.assertIn("url1", output)

    @patch('sys.stdout', new_callable=StringIO)
    def testApostropheHandlingPrint(self, mock_stdout):
        # Words with apostrophe for print

        self.searcher.printWord("joshua's")
        output = mock_stdout.getvalue()
        self.assertIn("7", output)
        self.assertIn("15", output)

    @patch('sys.stdout', new_callable=StringIO)
    def testCaseInsensitivityFind(self, mock_stdout):
        # Capitalization for find

        self.searcher.find("GoOd FrIeNdS")
        output = mock_stdout.getvalue()
        self.assertIn("url2", output)

    @patch('sys.stdout', new_callable=StringIO)
    def testCaseInsensitivityPrint(self, mock_stdout):
        # Capitalization for print

        self.searcher.printWord("NONSENSE")
        output = mock_stdout.getvalue()
        self.assertIn("6", output)


if __name__ == '__main__':
    unittest.main()
