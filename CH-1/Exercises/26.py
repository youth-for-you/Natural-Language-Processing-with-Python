# What does the following Python code do? sum(len(w) for w in text1)
#  Can you use it to work out the average word length of a text?
from nltk.book import *
if __name__ == '__main__':
    sumLen =sum(len(w) for w in text1)
    print("the average word length of a text is：%f" % (sumLen/len(text1)))