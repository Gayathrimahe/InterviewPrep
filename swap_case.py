#declare an empty string to swap case and update newly swapped String
#Use for loop to check each char case in the string and then swap upper case to lower and the vice versa
# and then add it to the result string

def swap_case(s):
    output = ''
    for char in s:
        if char.isupper():
            output += (char.lower())
        elif char.islower():
            output += (char.upper())
        else:
            output += char
    return output


print(swap_case('FkjhDDDDhl'))