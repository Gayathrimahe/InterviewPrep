class ReverseString:
    def reverse_sentence(self, sentence):
        self.sentence = sentence
        #string_list = reversed(sentence)# to reverse each character in string
        string_list = sentence.split()# convert sentence to list using split() method

        string_list.reverse()#reverse the list
        updated_list = string_list
        print(updated_list)

        new_sentence = ' '.join(updated_list)# use join iterables to string
        print(new_sentence)

test = ReverseString()

test.reverse_sentence("Welcome to Interview Preparation")
