'''
This returns the most frequent word -> returns a string -> in case of no setence - empty string

Flow:
1. from a sentence split the word
2. Purify the words - extract the verbal part - remove the ,.!? before and after
3. make sure to nomalise words - upper and lower is not different entity
4. get the ones which occur maximum number of times - and in case of tie, first come and first serve
'''

class Tools:
    '''
    Holds some functions which support the individual operation
    '''

    @staticmethod
    def return_words_in_sentence(sentence: str):
        '''
        the function returns the words and returns the filtered words
        '''
        raw_words = []

        for word in sentence.strip().split():
            word = word.strip(r"!?,.").lower()
            if word:
                raw_words.append(word)

        return raw_words


    @staticmethod
    def count_number_of_words(sentence: str):
        '''
        the function counts the number of unique words
        '''
        unique_words = {}

        words = Tools.return_words_in_sentence(sentence)

        for word in words:
            unique_words[word] = unique_words.get(word, 0) + 1

        return unique_words


    @staticmethod
    def most_occuring_word(sentence: str):
        '''
        This returns the word which occurs the maximum number of times
        '''
        if not sentence:
            raise ValueError("the sentence has no words")

        word_frequency = Tools.count_number_of_words(sentence)

        if not word_frequency:
            raise ValueError("the sentence has no comprehensible words")

        maxi_number = float("-inf")

        most_frequent_word = ""

        for word, frequency in word_frequency.items():
            if frequency > maxi_number:
                most_frequent_word = word
                maxi_number = frequency

        return most_frequent_word


def most_frequent_word(sentence): 
    return Tools.most_occuring_word(sentence)


def main():
    test_sentences = [
    "apple banana apple orange apple",
    "python is fun python is useful",
    "cat dog cat bird dog cat",
    "Python python PYTHON java Java",
    "Hello hello HELLO world",
    "hello, world! hello. world?",
    "Python, python! python.",
    "red, blue, red! green; red.",
    "cat dog dog cat",
    "apple banana banana apple",
    "one two three three two one",
    "Cat, dog! DOG cat.",
    "Python is great, python is useful. Java is great!",
    "",
    "     ",
    "hello",
    "!!! ??? ...",
    "the quick brown fox jumps over the lazy dog the fox is quick",
    "alpha beta gamma beta delta gamma gamma alpha"
    ]

    for sentence in test_sentences:
        try:
            print(f"The most frequent word in the sentence is : {most_frequent_word(sentence)}")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()


    

        
            


