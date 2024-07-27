experience = input("have you drove before?")
if experience != "yes" and experience != "no":
	print("please enter yes or no")
	raise SystemExit
age = input("whats your age?")
age = int(age)
if experience == "yes":
	if age >= 18:
		print("it's legal")
	else:
		print("it's illigal")
elif experience == "no":
	if age >= 18:
		print("you can take driving test")
	else:
		print("nice")
#else:
	#print("please enter yes or no")

