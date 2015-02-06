import os
import re

imgdir = "prank"

def rename_files():
    files = os.listdir(imgdir)

    renamed = []
    for file in files:
        renamed.append(stripnum(file))

    for file in renamed:
        print(file)

def stripnum(string):
    #My solution
    rename_regex = "[0-9]*(.*)"
    string = re.search(rename_regex, string).group(1)

    #Suggested solution
    #string = string.translate(None, "0123456789")

    return string
    

rename_files();
