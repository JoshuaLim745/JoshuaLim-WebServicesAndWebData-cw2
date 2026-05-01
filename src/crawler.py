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

import requests
from bs4 import BeautifulSoup
import time
import re
from urllib.parse import urljoin, urlparse

class Crawler:
    def __init__(self, startUrl, indexer):
        self.startUrl = startUrl
        self.baseDomain = urlparse(startUrl).netloc
        self.indexer = indexer

    def crawl(self):
        """Crawls the domain, extracts text, and builds the index."""
        visited = set()
        queue = [self.startUrl]
        self.indexer.index = {}  # Reset index before a fresh build

        print(f"Starting crawl at {self.startUrl}...")

        while queue:
            url = queue.pop(0)
            if url in visited:
                continue

            print(f"Crawling: {url}")
            visited.add(url)

            try:
                # Fetch the page
                response = requests.get(url, timeout=10)
                response.raise_for_status()
            except requests.RequestException as e:
                print(f"  [!] Failed to fetch {url}: {e}")
                continue

            # Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract text and convert to lowercase
            text = soup.get_text(separator=' ')
            
            # Tokenize: Find all words
            words = re.findall(r'\b\w+\b', text.lower())
            
            # Pass the extracted data to the indexer
            self.indexer.add_words(url, words)

            # Find all links on the page to continue crawling
            for link in soup.find_all('a', href=True):
                nextUrl = urljoin(url, link['href'])
                nextUrl = nextUrl.split('#')[0]  # Remove anchor fragments

                # Restrict crawling to the same domain
                if urlparse(nextUrl).netloc == self.baseDomain and nextUrl not in visited and nextUrl not in queue:
                    queue.append(nextUrl)

            # Observe the 6-second politeness window
            if queue: 
                print("[Politeness Window] Waiting 6 seconds...")
                time.sleep(6)

        # Save the populated index to the file system
        self.indexer.save()
        print(f"\nBuild complete. Index saved to {self.indexer.index_file}.")