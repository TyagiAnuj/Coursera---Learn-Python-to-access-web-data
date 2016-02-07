import urllib

fhand = urllib.urlopen('http://www.py4info.com/code/romeo.txt')
# quite similar to file handling, just reading file through socket

#for line in fhand:
#    print line.strip()
# get the content of the page, not http headers

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print counts
# now this is split the data on page by space and adding into dictionary
    
