# Write expressions for finding all words in text6 that meet the conditions listed below.
# The result should be in the form of a list of words: ['word1', 'word2', ...].
# a. Ending in ize
# b. Containing the letter z
# c. Containing the sequence of letters pt
# d. Having all lowercase letters except for an initial capital (i.e., titlecase)
from nltk.book import *
if __name__ == '__main__':
    words_a = []; words_b = []; words_c = []; words_d = []
    for w in text6:
        if w.endswith('ize'):
            words_a.append(w)
        if 'z' in w:
            words_b.append(w)
        if 'pt' in w:
            words_c.append(w)
        if w.istitle():
            words_d.append(w)
    print(words_a)
    print(words_b)
    print(words_c)
    print(words_d)
