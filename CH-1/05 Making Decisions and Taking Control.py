from nltk.book import *
if __name__ == '__main__':
    #4.1Conditionals 各种条件句
    #sent7来自华尔街日报
    print(sent7)
    #数值比较 <, <=, ==, !=, >, >=
    words = [w for w in sent7 if len(w) < 4]
    print(words)
    #词汇比较
    #s.startswith(t)    s是否以t开头
    #s.endswith(t)   s是否以t结尾
    #t in s     s是否包换t
    # s.islower()	s是否都是小写
    # s.isupper()	s是否都是大写
    # s.isalpha()	s是否都是字母
    # s.isalnum()	s是否都是数字和字母
    # s.isdigit()   s是否都是数字
    # s.istitle()    s是否首写字母大写
    #输出含有gnt的单词
    words1 = sorted(term for term in set(text4) if 'gnt' in term)
    print(words1)
    print(sorted(w for w in set(text7) if '-' in w and 'index' in w))
    #4.2   Operating on Every Element
    print([w.upper() for w in text1])
    #4.3   Nested Code Blocks
    word = 'cat'
    if len(word) < 5:
        print('word length is less than 5')
    #4.4   Looping with Conditions
    sent1 = ['Call', 'me', 'Ishmael', '.']
    for xyzzy in sent1:
        if xyzzy.endswith('l'):
            print(xyzzy)