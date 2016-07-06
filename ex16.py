from sys import argv
import time

script, file_name = argv

print "we are going to erase %r." % file_name
print "if you don't wish to continue plz pree ctrl + c"
print "if you want that hit return"

raw_input("??")

print "opening the file...."
target = open(file_name,'w')

print "truncating file......"
target.truncate()

print ("please enter content to write in %r" % file_name)

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print ("lines r adding iin ur %r" % file_name)

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("contents are saved in ur %r" % file_name)

print("opening the written content please wait it will take some time...")
time.sleep(25)

target_open = open(file_name,'r')
