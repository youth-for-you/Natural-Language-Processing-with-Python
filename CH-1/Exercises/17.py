#Use text9.index() to find the index of the word sunset.
#You'll need to insert this word as an argument between the parentheses.
#By a process of trial and error,
#find the slice for the complete sentence that contains this word.
from nltk.book import *
from numpy import *
if __name__ == '__main__':
    i = 0
    while i < len(text9):
        #没有用for循环是因为for循环不能改变循环变量i,因为range（）是一个迭代器只输出信息,不修改内容。
        if text9[i] == 'sunset':
            for j in range(i, 0, -1):
                if text9[j] == '.' or text9[j] == '?' or text9[j] == '!':
                    start = j+1
                    break
            for j in range(i, len(text9)):
                if text9[j] == '.' or text9[j] == '?' or text9[j] == '!':
                    end = j+1
                    i = end
                    break
            sent = text9[start: end]
            print('sentence start:%d, end:%d' % (start, end))
            print(' '.join(sent))
        else:
            i += 1



