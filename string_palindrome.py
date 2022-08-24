class String_Palindrome:
    def find_string_palindrome(self):
        user_string = input("Enter the string to find palindrome")
        revered_string = user_string[:: -1]
        if user_string == revered_string:
            print(f"{user_string} is palindrome")
        else:
            print(f"{user_string} is not palindrome")


test = String_Palindrome()
test.find_string_palindrome()