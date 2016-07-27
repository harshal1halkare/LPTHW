the_count = [1,2,3,4,5,6,7,8]
fruits = ['apples','graphes','orange','pears','gauva']
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
	print "this is count %d" %number

for fruit in fruits:
	print "the type of fruits are %r" %fruit

for i in change:
	print "here is the mix list %r" %i

elements = []

for i in range (0, 6):
	print "adding element to the list %i" %i
	elements.append(i)
	print(elements)
for i in elements:
	print "element was : %d" % i
