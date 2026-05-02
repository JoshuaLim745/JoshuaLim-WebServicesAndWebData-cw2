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

import sys
from indexer import Indexer
from crawler import Crawler
# from search import Searcher

def run_cli():
    # IMPORTANT: Replace this URL with the specific target site for your assignment
    TARGET_WEBSITE = "https://quotes.toscrape.com/" 
    
    # Initialize the components
    indexer = Indexer(indexFile='index.json')
    crawler = Crawler(TARGET_WEBSITE, indexer)
    # searcher = Searcher(indexer)

    print("--- Modular Search Tool Shell ---")
    print(f"Targeting: {TARGET_WEBSITE}")
    print("Available commands: build, load, print <word>, find <query>, exit")
    
    while True:
        try:
            user_input = input("> ").strip().split(maxsplit=1)
            if not user_input:
                continue

            command = user_input[0].lower()
            args = user_input[1] if len(user_input) > 1 else ""

            # Route commands to the appropriate module
            if command == 'build':
                crawler.crawl()
                
            elif command == 'load':
                success = indexer.load()
                if success:
                    print("Index loaded successfully.")
                else:
                    print(f"Error: '{indexer.indexFile}' not found. Please run 'build' first.")
                    
            elif command == 'print':
                if args:
                    # searcher.print_word(args)
                    print("print")
                else:
                    print("Usage error. Try: print <word>")
                    
            elif command == 'find':
                if args:
                    # searcher.find(args)
                    print("find")
                else:
                    print("Usage error. Try: find <query>")
                    
            elif command in ['exit', 'quit']:
                print("Exiting tool...")
                break
                
            else:
                print(f"Unknown command: {command}")
                
        except KeyboardInterrupt:
            print("\nExiting tool...")
            break

if __name__ == "__main__":
    run_cli()