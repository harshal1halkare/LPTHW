people = raw_input("please enter people count : ")
cars = raw_input("please enter cars count : ")
buses = raw_input("please enter buses count : ")

if cars > people:
	print "we shouold take cars"
elif cars < people:
	"we should not take this car"
else:
	"we can't decide"

if buses > cars:
	print "that's too many buses"
elif buses < cars:
	print "may be we could take the buses"
else:
	print "we still can't decide"

if people > buses:
	print "alright, let's just take the buses."
else:
	print "Fine ..let's stay home then"
