#Review 1 on computing with language.
#How many words are there in text2? How many distinct words are there?

from nltk.book import *
if __name__ == '__main__':
    print('text2单词数： %d' % len(text2))
    print('不重复单词数：%d' % len(set(text2)))