#The first sentence of text3 is provided to you in the variable sent3.
#  The index of the in sent3 is 1, because sent3[1] gives us 'the'.
# What are the indexes of the two other occurrences of this word in sent3?
from nltk.book import *
from numpy import *
if __name__ == '__main__':
    #print(sent3.index('the')),只能输出第一个匹配的索引
    for i in range(len(sent3)):
        if sent3[i] == 'the':
            print(i)