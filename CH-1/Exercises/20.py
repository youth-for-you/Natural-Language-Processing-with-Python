#What is the difference between the following two tests: w.isupper() and not w.islower()?
if __name__ == '__main__':
    test1 = 'I LVOE PYTHON !'
    test2 = 'I Love Python !'
    test3 = 'i love python !'
    #s.isupper()判断字符全都是大写，为真
    #not s.isupper()判断字符不全都是大写，为真
    print(test1.isupper())
    print(test2.isupper())
    print(not test2.isupper())
    print(not test3.isupper())