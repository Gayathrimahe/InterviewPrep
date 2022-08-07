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



test = Sort_List()
test.sort_list_elements([3, 7, 5, 9, 0])
test.sort_list_by_loop([89, 45, 23, 99, 55])