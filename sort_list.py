'''sort the list using sorted as well loop'''




class Sort_List:
    def sort_list_elements(self, iList):
        self.iList = iList
        print(sorted(iList))


    def sort_list_by_loop(self, input_List):
        self.input_List = input_List

        data_list = []
        while input_List:
            minimum = input_List[0]
            for x in input_List:
                if x < minimum:
                    minimum = x
            data_list.append(minimum)
            input_List.remove(minimum)
        print(data_list)


    def reverse_list(self, new_list):
        self.new_list = new_list
        print(new_list[:: -1])


    def reverse_through_loop(self, r_list):
        self.r_list = r_list
        length = len(r_list)
        rev_list = []
        for x in r_list:
            rev_list.append(r_list[length-1])
            length -= 1
        print(rev_list)




test = Sort_List()
test.sort_list_elements([3, 7, 5, 9, 0])
test.sort_list_by_loop([89, 45, 23, 99, 55])
test.reverse_list([54, 3, 5, 7, 11])
test.reverse_through_loop([9, 7, 3, 5, 1])