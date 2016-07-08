print "lets's practice everything"
print "yuo\'d neeed to knoe \'bout escape with \\ that do \n newlines and \t tabs."

poem = """
\t i dont know any
	but it is just to use \n
	i am on next line with the help of dat
	  """


print "==========================================="
print poem 
print "==========================================="


five = 10 - 2 + 3 - 6
print "this should be five : %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans,jars,crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)

print "with starting point of %r " % start_point
print "we would have %r jelly_beans %r jars % crates" %(beans,jars,crates)

start_point = start_point /10

print "we can do the same this way also"
print "we have %d beans %d jars %d crates" % secret_formula(start_point)

