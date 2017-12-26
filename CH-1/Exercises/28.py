# Define a function percent(word, text) that calculates how often a given word occurs in a text,
# and expresses the result as a percentage.
from nltk.book import *
def percent(word, text):
    """

    :param word:
    :param text:
    :return: calculates how often a given word occurs in a text
    """
    fdist = FreqDist(text)
    return fdist.freq(word)
def my_percent(word,text):
    """
    如果不引人nltk.book 不用FreqDist
    :param word:
    :param text:
    :return:
    """
    count = 0
    for w in text:
        if w == word:
            count += 1
    return (count/len(text))
if __name__ == '__main__':
    my_text = 'I love python and I try my best to learn it !'
    print(percent('I', my_text))
    print('%.3f%%' % (percent('I', my_text)*100))
    print('%.3f%%' % (percent('she', text1)*100))
