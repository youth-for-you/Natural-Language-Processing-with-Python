# Define sent to be the list of words
# ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore'].
#  Now write code to perform the following tasks:
#
#a. Print all words beginning with sh
#b. Print all words longer than four characters
if __name__ == '__main__':
    sent =['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
    sent_a = []; sent_b =[]
    for w in sent:
        if w.startswith('sh'):
            sent_a.append(w)
        if len(w) > 4:
            sent_b.append(w)
    print(sent_a) ;print(sent_b)

