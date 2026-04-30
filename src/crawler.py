"""
Requirements
1. Given base URl from main.py function call - quotes.toscrape.com
2. Scrape all the quotes on a page.
    a. Using beautifulSoup --> text = soup.get_text() --> full sentences but we are only interested in words.
    b. Using possibly either a regex or .split to remove all spaces, newlines, and punctuation except for apostrophe between words. Additionally, set use .lower() for all text.
    c. Words are then sent to the indexer.
3. Returing from the indexer, program looks for the 'Next page' button -- NOTE There are 10 pages.
    a. Using beautifulSoup --> find <a href="/page/<NUMBER>/"> element and user URLJoin to go to the next page to scrape .
    b. Websites that have already been visited are to be added to a list to prevent infinite looping of visits - Counters the 'Previous; page button.
4. Repeat steps 2 and 3 until all pages are scraped - There is to be a 6 second Politeness Window between page visits -- use time.sleep(6)
5. After all pages have been scraped call indexer to save/write the work to a .json file.
"""
