#What is the difference between the following two lines?
# Which one will give a larger value? Will this be the case for other texts?
from nltk.book import *
if __name__ == '__main__':
    print(len(sorted(set(w.lower() for w in text1))))
    print(len(sorted(w.lower() for w in set(text1))))
    #下面的大，下面的set（text1）是区分大小写的，同一个单词，大小写不同，他认为是不同的单词。
