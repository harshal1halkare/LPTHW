from sys import exit

def gold_room():
	print "this room is full of gold ..how much you take??"
	next = raw_input (">> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("please enter int value.............")
	
	if how_much < 50:
		print "nice your a nice guy not greedy one"
		exit(0)
	else:
		dead("this much greed is not good..........")

def bear_room():
	print "there is a beer here .."
	print "the beer has bunch of honey"
	print "the fat beeer is infront of door.. "
	print "how are you going to move beer \n"
	print "1. take honey ???"
	print "2. taunt bear ???"
	print "3. open door ???"
	bear_moved = False

	while True:
		next = raw_input(">>> ")
		if next == "take honey":
			print "congrats .... beer will slap you.."
		elif "taunt bear" and not bear_moved:
			print "wow bear moved.... you can go"
			bear_moved = True
		elif next == "taunt beer" and bear_moved:
			print "your dead "
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "invalid actions"
	
def cthulhu_room():
	print "here you will see great evil cthulhu....."
	print "he,it whatever stares at you and you go insane"
	print "do you flee for your life or will eat your head??? "
	
	next = raw_input(">>>> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("well that waz tasty..")
	else:
		cthulhu_room()


def dead(why):
	print why, "good job ...."
	exit(0)

def start():
	print "your in a dark room.."
	print "there is a door at your right and left choice is yours ....."
	print "which one you will take ?????"

	next = raw_input(">>>> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("you stumble around the room until you starve...")


start()
