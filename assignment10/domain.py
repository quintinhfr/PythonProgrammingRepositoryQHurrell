#domain.py

import sys
import stdio

# This program takes an internet link as a command line argument
# and prints it's domain type
# this program works with most standard https://www. URLS, there are links
# that it does not work with, but it works for most internet links

# Collect the link from the terminal

Link = str(sys.argv[1])

# Slit the list into different fragments by '.'

List = (Link.split('.'))

#Single out the fragment that contains the Domain Type

Specified = List[2]

# Now seperate the peices of the specified part of the URL

List2 = (Specified.split('/'))

# Create a variable containing the domain type

DomainName = List2[0]

#Print Domain Type

stdio.writeln(DomainName)