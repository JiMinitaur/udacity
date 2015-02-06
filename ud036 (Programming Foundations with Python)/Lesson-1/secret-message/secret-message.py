import os
import re

imgdir = "prank"

def rename_files():
    files = os.listdir(imgdir)

    renamed = []
    for file in files:
        newname = stripnum(file)
        #os.rename(file, newname)
        renamed.append(newname)

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
