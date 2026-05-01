"""
AI helped here as I am unsure on how the test cases would look with mock websites
Cases
Basic functionality
1. Scraping of a mock website (Some simple HTML should do it)
    a. Check that the list created by indexer is equal to the expected list. In terms of [word][URL]: [position(s)]
    b. Visually check for removal of punctuation that is not needed
2. Check for capablity to find links -- 
    a. Simulate a mock website with an element of the <a href='/page2'>Link</a>
    b. 2 requests should have been made to the mock website
    c. Check that the program actually tried to visit the constructed page

Edge cases
1.
"""

import unittest 
import sys
import os
from unittest.mock import patch, MagicMock
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.crawler import Crawler
from src.indexer import Indexer


class testCrawler(unittest.TestCase):
    def setUp(self):
        self.indexer = Indexer()
        self.crawler = Crawler("http://test.com", self.indexer)

    # We patch requests.get to fake the HTML response, and time.sleep to skip the 6-second wait
    @patch('src.crawler.requests.get')
    @patch('src.crawler.time.sleep')
    def testCrawlExtractsWords(self, mock_sleep, mock_get):
        # Creating a fake response object
        mock_response = MagicMock()
        mock_response.text = "<html><body><p>Hello world! Hello test.</p></body></html>"
        mock_get.return_value = mock_response

        # Run the crawl (it should only crawl the start URL since there are no links)
        self.crawler.crawl()

        # Check if words were extracted and passed to the indexer correctly
        # Ignoring punctuation and converting to lowercase
        expected_index = {
            "hello": {"http://test.com": [0, 2]},
            "world": {"http://test.com": [1]},
            "test": {"http://test.com": [3]}
        }
        self.assertEqual(self.indexer.index, expected_index)

    @patch('src.crawler.requests.get')
    @patch('src.crawler.time.sleep')
    def test_crawl_finds_links(self, mock_sleep, mock_get):
        # First page has a link to page2, page2 has no links
        responses = [
            MagicMock(text="<html><a href='/page2'>Link</a></html>"),
            MagicMock(text="<html>End here</html>")
        ]
        mock_get.side_effect = responses

        self.crawler.crawl()

        # It should have called requests.get twice
        self.assertEqual(mock_get.call_count, 2)
        # Check that it actually tried to visit the constructed URL
        mock_get.assert_any_call("http://test.com/page2", timeout=10)
        
        # Checks if the time.sleep(6) was called. If so then it marks the assert as a success and ignores the 6 second wait time
        mock_sleep.assert_called_with(6)

if __name__ == '__main__':
    unittest.main()