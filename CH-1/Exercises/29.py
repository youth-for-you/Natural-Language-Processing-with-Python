# We have been using sets to store vocabularies.
# Try the following Python expression: set(sent3) < set(text1).
# Experiment with this using different arguments to set().
# What does it do? Can you think of a practical application for this?
from nltk.book import *
if __name__ == '__main__':
    no_sent3 =set(text1) - set(sent3)
    #我们可以输出不在sent3 的存在在text1 的词汇等等
    print(no_sent3)