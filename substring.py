'''
program to get the n (non-negative integer) copies of the first 2 characters of a given string.
Return the n copies of the whole string if the length is less than 2
'''

class Substring_string:
    def copy_char(self, str, n): # str -->input string -->no.of.copies
        self.str = str
        self.n = n
#finding substring for 1st 2 character of input string(str)
        s_len = 2
        if s_len > len(str):
            s_len = len(str)
        substring = str[:s_len]
#taking copies of substring
        copy_string = ""
        for i in range(n):
            copy_string += substring
        print(copy_string)


test = Substring_string()
test.copy_char('welcome', 2)