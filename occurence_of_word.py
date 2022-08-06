''' Pgm to count number of occurance of word in a sentence
--->input sentence to find occurance/
--->initialise count as dictionary to read word as key and occ as value
---->iterate through sentence to find the count of words
---->sentence.split() is used to convert sentence to list of words ,if split is not used then it
displays occurances of letters'''


class Word_Occurance:
    def occ_of_words(self, sentence):
        self.sentence = sentence
        sentence = sentence.split()
        count = dict()
        for word in sentence:
            if word in count:
                count[word] += 1
            else :
                count[word] = 1

        return count

test = Word_Occurance()
print(test.occ_of_words("Welcome to Interview preparation.Prepare to succeed"))

