# Review the discussion of looping with conditions in 4.
# Use a combination of for and if statements to loop over the words of the movie script
# for Monty Python and the Holy Grail (text6) and
# print all the uppercase words, one per line.
from nltk.book import *
if __name__ == '__main__':
    for w in text6:
        if w.isupper():
            print(w)