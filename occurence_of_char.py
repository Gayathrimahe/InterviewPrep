my_string = input("Enter the string")
my_char = input("Enter the character")
count = 0
for x in range(0, len(my_string)):
    if(x == my_char):
        count +=1
print(f"{count}")