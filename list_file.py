'''
You can use this method if you want to write a list of items and do not want to iterate through the list of items.

This method doesn’t add any line separators. Hence, all the list items are added in a single line.

Similar to the write() method, you can open the file in the write mode and invoke the writelines()
method to write the list to the file.
'''

colours = ['Orange', 'White', 'Green', 'Blue']
with open('list_of_colours.txt', 'w') as f:
    f.writelines(colours)