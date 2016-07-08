people = raw_input("please enter people value")
cats = raw_input("please enter cats value")
dogs = int(raw_input("please enter dogs value"))

if people < cats:
	print "too many cats! The world is doomed!"
if people > cats:
	print "Not many cats ! The world is saved"
if people < dogs:
	print "The world is full of dogs"
if people > dogs:
	print "too many human"

dogs += 5

if people >= dogs:
	print "people are greater than or equal to dogs"
if people <= dogs:
	print "people are less than equal to dogs."
if people == dogs:
	print "people are dog"
