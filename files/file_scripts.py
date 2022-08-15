'''python scripts instead of bash scripts
>> to view all the files in the path specified'''


import os
path = 'C:/aws/interview questions'
with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)