import string

class Alphabet_case:
    def uppercase_letters_file_line(self, n):
        self.n = n
        with open("words1.txt", "w") as f:
            u_alphabet = string.ascii_uppercase
            letters = [u_alphabet[i:i + n] + "\n" for i in range(0, len(u_alphabet), n)]
            f.writelines(letters)

    def lowercase_letters_file_line(self, n):
        self.n = n
        y = open("words1.txt", "w")
        l_alphabet = string.ascii_lowercase
        letters = [l_alphabet[i:i + n] + "\n" for i in range(0, len(l_alphabet), n)]
        y.writelines(letters)


test = Alphabet_case()
test.uppercase_letters_file_line(4)
#test.lowercase_letters_file_line(3)

