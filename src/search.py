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