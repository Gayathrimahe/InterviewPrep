# given string must be split and converted to a list then add a delimiter '-' and join the strings
#use Split() method to remove space and convert to list
#use join method to join strings in a list with a delimiter


def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)