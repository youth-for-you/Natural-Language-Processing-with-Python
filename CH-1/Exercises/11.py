#Define several variables containing lists of words,e.g., phrase1, phrase2, and so on.
#Join them together in various combinations (using the plus operator) to form whole sentences.
#What is the relationship between len(phrase1 + phrase2) and len(phrase1) + len(phrase2)?

if __name__ == '__main__':
    phrase1 = ['I', 'Love', 'Python', '!']
    phrase2 = ['Do', 'You', 'Love', 'Python', '?']
    phrase = phrase1 + phrase2
    print(phrase)
    print(len(phrase1)+len(phrase2), len(phrase))