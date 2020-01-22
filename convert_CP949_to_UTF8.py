from pathlib import Path
import os
path = 'web'
filetypes = ['*.html','*.css','*.js']
for filetype in filetypes:
    for filename in Path(path).rglob(filetype):
        command = f'iconv -f CP949 -t UTF-8 -o {filename} {filename}'
        print(command)
        #os.system(command)
