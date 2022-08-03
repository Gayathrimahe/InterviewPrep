'''for reversal of words in sentence or names ,convert them to list and use reverse ()
once reversed use .join to return to original string format with space or any delimiter in quotes'''

class ReverseName:
    def reverse_name(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        combined_name = [firstName, lastName]
        combined_name.reverse()
        return ' '.join(combined_name)
    def reverse_whole_string(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        c_name = f_name +" "+ l_name
        return c_name[ :: -1]#slice [::-1] reverses whole string




name = ReverseName()
print(name.reverse_name('Gayathri', 'Mahendran'))
print(name.reverse_whole_string('gayathri', 'mahendran'))
