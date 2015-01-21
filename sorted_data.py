"""Write a program that reads the file, then spits out the ratings in 
alphabetical order by restaurant 

open file
add each line to a dictionary
list restaurants in alphabetical order
use for loop to go through each item in list

"""

our_file = open('scores.txt')

dictionary = {}

for line in our_file:
    line = line.rstrip()
    entries = line.split(":")
    name = entries[0]
    score = int(entries[1])
    dictionary[name] = score

sorteddict = sorted(dictionary.iteritems())

for item in sorteddict:
    print "%r is rated at %r." % (item[0], item[1])
