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

