import os
import re
from operator import itemgetter

def main():
    imgdir = "prank"
    files = os.listdir(imgdir)

    tuples = []
    for file in files:
        ## get string for modified filename
        newname = stripnum(file)

        ## lesson recommended path
        #os.rename(file, newname)

        ## immutable source files option        
        tuples.append((newname, file))

    ## My first lambda (awwwwww, how cute)
    ## Sorts the data structure, saving both versions of filename
    sorteds = sorted(tuples, key=lambda tuple: tuple[0])
    for tuple in sorteds:
        print(tuple);

    ## generates html
    write_output(sorteds)

def stripnum(string):
    ## My solution
    rename_regex = "[0-9]*(.*)"
    string = re.search(rename_regex, string).group(1)

    ## Suggested solution
    #string = string.translate(None, "0123456789")

    return string

def write_output(tuples):
    sources = "../prank/"
    location = "output/"
    target = location + "output.html"

    if not(os.path.isdir(location)):
        os.mkdir("output")
    output = open(target,"w")
    html_open(output)

    for tuple in tuples:
        output.write("<img src='")
        output.write(sources)
        output.write(tuple[1])
        output.write("""' />
        """)
    
    html_close(output)
    output.close()

    import webbrowser
    webbrowser.open(os.path.abspath(target))

def html_open(file):
    file.write("""
        <!DOCTYPE html>
        <html>
        <head>
        <title>Secret Message</title>
        <style>img {max-height=100px; max-width:100px}</style>
        </head>
        <body>
        """)

def html_close(file):
    file.write("""
        </body>
        </html>
        """)


main()
