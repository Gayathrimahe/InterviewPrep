'''

'''



import heapq as hq

class Small_Largest:
    def largest_3_num(self, input_list):
        self.input_list = input_list
        sorted_list = hq.nlargest(3, input_list)
        print(sorted_list)


    def smallest_3_num(self, i_List):
        self.i_List = i_List
        s_List = hq.nsmallest(4, i_List)
        print(s_List)


test = Small_Largest()
test.largest_3_num([65, 23, 66, 97, 11, 34])
test.smallest_3_num([9, 4, 6, 12, 1])