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
            "nonsense": {"url1": [1, 2, 3, 4, 5, 6]}
        }
        self.searcher = Searcher(self.indexer)

    @patch('sys.stdout', new_callable=StringIO)
    def testFindSingleWord(self, mock_stdout):
        self.searcher.find("good")
        output = mock_stdout.getvalue()
        
        self.assertIn("url1", output)
        self.assertIn("url2", output)
        self.assertNotIn("url3", output)

    @patch('sys.stdout', new_callable=StringIO)
    def testFindMultipleWords(self, mock_stdout):
        # should return url2 as it has both good and friends
        self.searcher.find("good friends")
        output = mock_stdout.getvalue()
        
        self.assertIn("url2", output)
        self.assertNotIn("url1", output)
        self.assertNotIn("url3", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_find_no_results(self, mock_stdout):
        self.searcher.find("aliens")
        output = mock_stdout.getvalue()
        self.assertIn("No pages found.", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_word_frequency(self, mock_stdout):
        self.searcher.printWord("nonsense")
        output = mock_stdout.getvalue()

        # 'nonsense' appears 6 times in url1
        self.assertIn("Frequency: 6", output)
        self.assertIn("Positions: [1, 2, 3, 4, 5, 6]", output)

if __name__ == '__main__':
    unittest.main()
