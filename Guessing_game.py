num = 0
i = 1
while i < 11:
	num = int(raw_input("enter your number"))
	if num == 5:
		print "guess kar liye"
		break
	if num<5:
		print "chota hain"
	if num>5:
		print "bada hain"
	else:
		print "guess nhi kar paaye ho"
		
