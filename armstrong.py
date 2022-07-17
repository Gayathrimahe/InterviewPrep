#to find armstrong number or not the sum of cubes of each digit in number
# should be equal to number itself eg. 153 = 1^3 + 5^3 +3^3
def find_armstrong_num():
    #create a empty list to append each digit as separate integers
    my_list = []
    num = int(input("Enter the number to find if its armstrong number or not:"))
    #num = 153
    #int cannot be iterated so its converted to str and then each digit is stored as int in list
    for x in str(num):
        my_list.append(int(x))
    print(my_list)

    arm = list(map(lambda x: x ** 3, my_list))
    print(sum(arm))
    if num == sum(arm):
        print(f"{num} is armstrong number")
    else:
        print(f"{num} is not armstrong number")
#print(num_list)


find_armstrong_num()