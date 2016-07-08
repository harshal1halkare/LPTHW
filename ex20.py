from sys import argv
import time

script,input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count,f):
	print line_count, f.readline()

current_file = open(input_file)

print "first let's print the whole file \n"

print_all(current_file)


time.sleep(15)

print "now let us rewind it"

rewind(current_file)

time.sleep(15)

print "lets print three line"

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

