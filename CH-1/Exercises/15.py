#Review the discussion of conditionals in 4.
# Find all words in the Chat Corpus (text5) starting with the letter b.
# Show them in alphabetical order.
from nltk.book import *
if __name__ == '__main__':
    print(sorted(set([w for w in text5 if w.startswith('b')])))