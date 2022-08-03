'''for reversal of words in sentence or names ,convert them to list and use reverse ()
once reversed use .join to return to original string format with space or any delimiter in quotes'''

class ReverseName:
    def reverse_name(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        combined_name = [firstName, lastName]
        combined_name.reverse()
        return ' '.join(combined_name)


name = ReverseName()
print(name.reverse_name('Gayathri', 'Mahendran'))
