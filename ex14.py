from sys import argv

script, user_name = argv
prompt = '>'

print "hi %s, I'm the %s script." %(user_name,script)
print "I'd like to ask you a few questions."

likes =str(raw_input("Do you like me %s %s" % (user_name ,prompt)))
print(likes)

lives =str(raw_input("where do you live %s %s ?" %( user_name,prompt)))
print(lives)

computer =str(raw_input("what kind of computer do you have %s %s? " %( user_name,prompt)))
print(computer)

print """ Alright, so you said %r about liking me.
	  you live in %r. I know where it is.
	  and you have a %r computer. Nice
	""" %(likes,lives,computer)


