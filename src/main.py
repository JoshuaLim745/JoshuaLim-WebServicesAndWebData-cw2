"""
Requirements
1. Varaible creation and assignments
    a. website URL - quotes.toscrape.com
    b. Obj creation for indexer, crawler, and search
2. While loop --> while true
    a. Waits for user input
    b. Accepts input --> splits it into 2 parts. Command and args
    c. if elif else for all 4 commands (build, load, print, find), a way to exit the program, and a message to tell the user that the command entered is incorrect. 
    d. Each of the 4 commands will call upon a specific function:
        build --> crawler.crawl()
        load --> indexer.load()
        print --> search.print(args)
        find --> search.find(args)

        extra
        exit --> breaks the infinite while loop
        else --> Incorrect input entered
"""