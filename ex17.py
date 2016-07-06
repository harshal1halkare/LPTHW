from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" %(from_file,to_file)

target = open(from_file,'r')
in_file = target.read()
print "the input file is %r bytes long" % (len(in_file))

print "does the output file exists? %r" % exists(to_file)
print "Ready?, hit return to continue, cntrl + c to abort"
raw_input()

out_file = open (to_file,'w')
out_file.write(in_file)

print "all done....."

out_file.close()
target.close()
