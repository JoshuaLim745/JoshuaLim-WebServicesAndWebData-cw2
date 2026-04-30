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