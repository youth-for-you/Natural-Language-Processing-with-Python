#Using list addition, and the set and sorted operations,
#compute the vocabulary of the sentences sent1 ... sent8.
from nltk.book import *
if __name__ == '__main__':
    voc = []
    for sent in [sent1, sent2, sent3, sent4, sent5, sent6, sent7, sent8]:
        voc += sent
    print(sorted(set(voc)))

