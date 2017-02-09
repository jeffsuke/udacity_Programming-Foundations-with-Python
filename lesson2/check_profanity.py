import os
import urllib

def read_text():
    quotes = open(os.path.join(os.getcwd(), 'movie_quotes.txt'))
    contens_quotes = quotes.read()
    # print(contens_quotes)
    quotes.close()
    check_profanity(contens_quotes)

def check_profanity(text_to_check):
    # urlopen is similar to open. Thus, we can also read the output
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    connection.close()

    if "true" in output:
        print("Profanity Alert")
    elif "false" in output:
        print("This document has no curse words.")

read_text()
