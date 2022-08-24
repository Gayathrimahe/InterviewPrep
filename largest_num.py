'''Find the kth largest number in arr
sort the given array and find kth largest num'''

class Largest_num:
    def finding_largest_num(self, arr):

        self.arr = arr
        element = int(input(f"Enter the  largest  to find"))
        sorted_arr = sorted(arr)
        print(sorted_arr)
        print(f"the {element} largest element in given sorted array is {sorted_arr[element - 1]}")


test = Largest_num()
test.finding_largest_num([5, 3, 8, 2, 9])