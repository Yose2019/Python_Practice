# the program counts the number of times a word has appreared in a string
# the assumption is there are only spaces and other punctuations are not considered 

def countWordFrequency(s : str):
    s = s.split(' ')
    freq = {}

    for word in s:
        word = word.lower()
        freq.setdefault(word, 0)
        freq[word] += 1

        '''
        freq[word] = freq.get(word, 0) + 1 is also valid
        '''

    print(freq)

countWordFrequency("Happy birthday to you stay happy")
