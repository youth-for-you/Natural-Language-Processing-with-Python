# Define a function called vocab_size(text) that has a single parameter for the text,
#     and which returns the vocabulary size of the text.
from nltk.book import *
def vocab_size(text):
    return len(text)
if __name__ == '__main__':
    print(vocab_size(text1))