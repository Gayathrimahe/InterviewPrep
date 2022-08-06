''' glob is used to search files /folders whose name follows a specific pattern, its similar to
unix shell path expansion rules.
Asterisk (*): Matches zero or more characters
Question Mark (?) matches exactly one character
We can specify a range of alphanumeric characters inside the [].

Set recursive=True to search inside all subdirectories. It is helpful If we are not sure exactly in which folder our search term or file is located.
 it recursively searches files under all subdirectories of the current directory

 Default recursive is set False'''

import glob

# path to search all txt files
path = "C:/aws/SSIS/sample_files/*.csv"
files = glob.glob(path, recursive=True)
print(files)