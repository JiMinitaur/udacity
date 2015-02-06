import os
import re

imgdir = "prank"
rename_regex = "[0-9]*(.*)"

def rename_files():
    files = os.listdir(imgdir)

    renamed = []
    for file in files:
        renamed.append(stripnum(file))

    for file in renamed:
        print(file)

def stripnum(string):
    string = re.search(rename_regex, string).group(1)
    return string
    

rename_files();
