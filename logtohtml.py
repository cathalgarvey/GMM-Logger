#!/usr/bin/env python3
# Takes a csv logfile and simply formats it into a HTML table.
from sys import argv
# Get arguments:
def usage():
    print("logtohtml.py - A simple csv-tabular html converter written as part of GMM Logger\nby Cathal Garvey (https://github.com/cathalgarvey/GMM-Logger)\n Usage: logtohtml.py [csv-formatted-logfile]\n HTML-formatted logfile will be saved to script directory.")
    exit()

if len(argv) != 2:
    usage()

if (argv[1].lower() == '-h') or (argv[1].lower() == '--help'):
    usage()

LogName = argv[1]
print("File to be processed: "+argv[1])

# Some definitions for later:
HTMLPrefix = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="robots" content="noindex" />
  <title>'''+LogName+'''</title>
</head>
<body>
<table border=1>'''

HTMLSuffix = '''</table>
<footer>
<p>Created with <a href="https://github.com/cathalgarvey/GMM-Logger">GMM Logger</a>, &copy; 2012 <a href="http://www.indiebiotech.com">Cathal Garvey</a>. Python code released under the <a href="https://www.gnu.org/licenses/gpl.html">GNU GPL</a>, Log Templates released under <a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>.</p>
  </footer>
</body>
</html>'''

def TabulateCSVLine(Line):
    'Takes a comma-separated line and reformats to Tabular HTML for insertion into a HTML list.'
    HTMLcols = ['<tr>']
    SplitLine = Line.split(",")
    for Column in SplitLine:
        NewCol = "<td>"+Column+"</td>"
        HTMLcols.append(NewCol)
    HTMLcols.append("</tr>\n")
    return "".join(HTMLcols)

# The action happens here:
HTMLifiedLogName = LogName.split(".")[0] + ".html" # Chop off .csv file ext., use .html instead

with open(LogName, encoding='utf-8', mode='r') as LogFile:
    LogContents = LogFile.read()

LogLines = LogContents.split("\n")
NewLines = []
for Line in LogLines:
    NewLines.append(TabulateCSVLine(Line))

HTMLedLogTable = HTMLPrefix + "\n".join(NewLines) + HTMLSuffix

with open(HTMLifiedLogName, encoding='utf-8', mode='w') as HTMLog:
    HTMLog.write(HTMLedLogTable)
print("Done!")
