print "You enter a dark room with two door's. Which door you will prefer door #1 or door #2"

door = raw_input ("waiting for your choice.. >>> ")

if door == "1" :
	print "there is a giant bear ...your game over haha... WHAT YOU WILL DO NOW ?"
	print "1. You will run?"
	print "2. or you will fight with him ? "
	
	bear = raw_input("commomn be fast you have less time ... Tell me ??")
	
	if bear == "1":
		print "You made a rite choice... good job"
	elif bear == "2" :
		print "your brave heart"
	else:
		print "your making wrong choice dude"

elif door == "2" :
	print "here you will meet a tiger.."
	print "now what you will do ?"
	print "1. fight with him ?"
	print "2. run away ?"
	print "3. or will take my advice?"
	
	tiger = raw_input("enter choice no other option >>>>")
	
	if tiger == "1" :
		print "u can win"
	elif tiger == "2" :
		print "he is comming for you don't run ... fight "
	elif tiger == "3" :
		print "my advice is why you entered here go back and choose door 1"
	else:
		print "your making wrong choice dude"
else:
	print "atleast select one option ... "
