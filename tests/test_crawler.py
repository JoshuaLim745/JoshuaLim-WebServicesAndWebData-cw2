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