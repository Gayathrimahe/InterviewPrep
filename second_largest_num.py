# finding second largest and second smallest number in a list
#using sort and negative indexing to return second largest

def sec_large_small():
    list = [45, 32, 67, 21, 43]
    list.sort()
    print(list[-2])

sec_large_small()

# same way sort the list ,use remove and max function to
# remove highest number from list then print second highest number
def finding_sec():
    list = [43, 21, 32, 89, 65]
    list.sort()
    list.remove(max(list))
    print(max(list))

finding_sec()


