#!/usr/bin/env python3
# Takes a csv file, reads the top line (column titles), and simply provides friendly inputs for
# each item. Then concatenates each entry with commas and appends to log as a new line.
from sys import argv

def usage():
    print("logentry.py - A simple csv-logfile utility written as part of GMM Logger\nby Cathal Garvey (https://github.com/cathalgarvey/GMM-Logger)\n Usage: logentry.py [csv-formatted-logfile]\n A prompt will guide you through appending a log entry.")
    exit()

if len(argv) != 2:
    usage()

if (argv[1].lower() == '-h') or (argv[1].lower() == '--help'):
    usage()

with open(argv[1], encoding='utf-8', mode='r') as LogFile:
    LogContents = LogFile.read()
FirstLine = LogContents.split("\n")[0]

NewLine = []
for Column in FirstLine.split(","):
    EntryVal = input("New Value for '"+Column.strip()+"':\n > ")
    EntryVal = EntryVal.replace(",","") # strip out any commas the user may have added. Silly user.
    NewLine.append(EntryVal)

NewLineString = ",".join(NewLine) # Creates a new comma-delimited line from NewLine list items.
with open(argv[1], encoding='utf-8', mode='a') as LogFile:
    LogFile.write('\n'+NewLineString)
