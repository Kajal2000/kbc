i = 0
sum = 0
while i < 11:
	weight =int(raw_input("enter your number"))
	sum = sum + weight
	i = i + 1
print sum
if sum % 5 == 0:
	print "5 se disivile h"
else:
	print "5 se disivile nhi h"
