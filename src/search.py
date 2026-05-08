"""
Requirements
1. Print function
    a. Input parameter - word
    b. .lower it (could be done in main?)
    c.  Check for word existance in the index
        if exist print URl, position, frequency on the URL
        Else return error message to annouce that the word was not found in the index

2. Find function
    a. Input parameter - word(s)
    b. Split word(s) into a list and .lower() them
    c. Work on the first word in the query
        i. Check for existance of word
            1. If exist get all keys related to the pages that the word can be found in and add this to a set / list. To be used for comparison
            2. Else return error message for word not in index.
    d. For loop that excludes the first word in the index. (list slicing?)
        i. Existance check
            1. If exist
                a. Get all keys related to the pages that the word can be found in
                b. Check for intersection with the URLs in the list / set of word[0]
                c. Update the word[0] list accordingly
            2. Else return error message for word not in index. 
        ii. Repeat this loop until the end of the args
    e. Return all the URL of pages where all the words appear on - If there is no pages then just return with an appropraite message stating as such. 

"""

class Searcher:
    def __init__(self, indexer):
        self.indexer = indexer

    def printWord(self, word):
        """Prints the index entries (URLs, frequencies, and positions) for a single word."""

        word = word.lower()
        if word in self.indexer.index:
            print(f"\nInverted index for '{word}':")
            for url, positions in self.indexer.index[word].items():
                frequency = len(positions)
                print(f"  -> {url} (Frequency: {frequency}, Positions: {positions})")
        else:
            print(f"The word '{word}' was not found in the index.")



    def find(self, query):
        """Finds URLs that contain all words in the provided query phrase (AND logic)."""
        words = query.lower().split()

        # Start with the URLs containing the first word
        if words[0] not in self.indexer.index:
            print("No pages found.")
            return

        # Keep a mathematical set of matching URLs to filter down
        matchingUrl = set(self.indexer.index[words[0]].keys())

        # Intersect with URLs containing subsequent words
        for word in words[1:]:
            if word not in self.indexer.index:
                print("No pages found.")
                return
            matchingUrl.intersection_update(set(self.indexer.index[word].keys()))

        if matchingUrl:
            print(f"\nPages containing '{query.lower()}':")
            for url in matchingUrl:
                print(f"  -> {url}")
        else:
            print("No pages found.")