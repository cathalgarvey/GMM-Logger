# GMM-Logger
A set of log templates, and a pair of handy scripts, for managing logs for a GMO/GMM containment lab.

## What is this?
One common, perhaps immutable requirement of GMO containment labs in Europe and elsewhere is the maintenance of accurate, and often extensive, logs. Rather than keeping paper logs, which are cumbersome, costly and hard to process, archive and send, I elected to keep simple tabular [csv-formatted](https://en.wikipedia.org/wiki/Comma_separated_values "Wikipedia entry for CSV format") logfiles.

To make management of these logs easier, I created a pair of simple python 3 scripts: one to append new lines to a specified csv log, and another to take a simple csv log and convert it to a simple HTML-formatted log, for ease of reading and sharing with regulatory bodies or interested persons.

These scripts should work fine on any platform with Python 3 installed, but there may be some oddities due to my specific usage of Unix line endings. HTML rendering should not be affected.

## Usage
You must have python 3 installed to use these utilities. You can either invoke them directly if using Linux (i.e. using "./logentry [file]"), or on other systems you can invoke them using the python interpreter (I believe "python3 logentry [file]" should work on all platforms that have Python 3 installed).

### logentry.py
Usage: logentry.py [csv-formatted-logfile]

logentry.py simply takes the top line of a csv file and assumes this line contains column titles. Each column title is presented in a prompt to the user for the new entry's value in that column. Entries are sanitised for commas, to prevent users accidentally creating new columns while providing an entry. Once all column entries have been provided, a new line is formatted and appended to the target log file.

logentry.py prepends the new line with a Unix newline character, "\n". On some systems that fail to understand such simple standards, this may lead to logs appearing to run along one continuous line. logtohtml.py will probably nevertheless interpret and format these files correctly, as it internally delimits lines using the "\n" character rather than relying on local system norms.

### logtohtml.py
Usage: logtohtml.py [csv-formatted-logfile]

logtohtml.py extracts each line of the provided logfile, and splits the file by unix newline characters ("\n") to get each "row" of the csv table. For each row, it then splits by comma (",") to get entries. Every entry is wrapped with html list entry flags, and is placed in a new line wrapped in list row flags. Each row formatted in this way is placed in a pair of html "table" tags to create a simple table, and this table is in turn placed in a basic HTML-5 compliant HTML page with the original document's name as window title.

This page is saved using the same name as the processed log, but with the .html file extension replacing the prior extension.

## Potential Improvements
### Superscripting
It would be pretty straightforward to create a more advanced script that prompts users to select a log to edit, prompts them to add a new entry, and then saves a HTML copy to another directory. That would make log maintainence a more interactive process and one with fewer steps required.

### Web Interface
Further to the above, the actual selection and editing of log contents could be performed through a CherryPy-driven web server. This could take the form of a script that launches the server, launches a page in the system browser to load the served pages, and provides a simple interface for log management.

### Timestamping and Local-Global Time Conversions
Given the increasingly global scope of biotech, collaborations are becoming more common across timezones. It's unlikely that regional time differences and logfile entries will be very important to collaborators for the most part. However, for niche cases it could be interesting to create an automatic date/time extraction system using Regular Expressions or column-name detection, and import dates/times to native Python Format for conversion to international time standards like UTC. This would allow easy comparisons of Logged events without having to consider timezone differences.
