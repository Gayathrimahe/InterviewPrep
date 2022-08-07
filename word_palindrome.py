'''If the given word is same even after reversing then its palindrome
using reverse() won't work on string ,so use negative slicing or looping through string to reverse
word and then compare'''


class Word_Palindrome:
    def find_word_palindrome(self, word):
        self.word = word
        reversed_string = word[::-1]
        print(reversed_string)
        if word == reversed_string:
            print("given word is palindrome")
        else:
            print("Given word is not palindrome")

test = Word_Palindrome()
test.find_word_palindrome("madam")