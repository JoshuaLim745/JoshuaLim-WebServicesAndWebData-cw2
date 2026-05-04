"""
Cases
Basic functionality
1. Add words to the list
    a. Check for word, URL, frequency, and position --> assert (Check existance, and the correct position and frequency)
2. Save and Load
    a. Create an indexer and simulate adding dummy data.
    b. Save it and check for the .json file's existance.
    c. Create a new indexer and laod the created dummy test file.
    d. Check for the value loaded into the new indexer to ensure that it returns expected value
3. Loading of a .json file that doesn't exist
    a. indexer is to attempt to load the file
    b. the value status returned by the load function should be false due to the .json file not exisiting
"""

import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.indexer import Indexer


class TestIndexer(unittest.TestCase):
    def setUp(self):
        # Use a temporary test file so we don't overwrite the real index
        self.testFile = 'testIndex.json'
        self.indexer = Indexer(indexFile=self.testFile, testCase=True)

    def tearDown(self):
        # Clean up the test file after tests run
        if os.path.exists(self.testFile):
            os.remove(self.testFile)

    def testAddWords(self):
        url = "http://test.com"
        words = ["hello", "world", "hello"]
        self.indexer.addWords(url, words)

        # 'hello' should be at positions 0 and 2
        self.assertIn("hello", self.indexer.index)
        self.assertEqual(self.indexer.index["hello"][url], [0, 2])
        
        # 'world' should be at position 1
        self.assertIn("world", self.indexer.index)
        self.assertEqual(self.indexer.index["world"][url], [1])

    def testSaveAndLoad(self):
        # Populate dummy data
        self.indexer.index = {"test": {"http://test.com": [0]}}
        
        # Save it
        self.indexer.save()
        self.assertTrue(os.path.exists(self.testFile))

        # Create a new indexer to test loading
        new_indexer = Indexer(indexFile=self.testFile, testCase=True)
        success = new_indexer.load()

        self.assertTrue(success)
        self.assertEqual(new_indexer.index, {"test": {"http://test.com": [0]}})

    def testLoadFileNotFound(self):
        # Ensure it handles a missing file gracefully
        success = self.indexer.load()
        self.assertFalse(success)

if __name__ == '__main__':
    unittest.main()
