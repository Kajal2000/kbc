#num1 = (raw_input("enter your number"))
#num2 = (raw_input("enter your number"))
#num3 = (raw_input("enter your number"))
#if num1 >= num2:
#	largest = num1
#elif num2 >= num3:
#	largest = num2
#else:
#	largest = num3
#
#print largest


num1 = (raw_input("enter your number"))
num2 = (raw_input("enter your number"))
num3 = (raw_input("enter your number"))

if num1 <= num2 or num2 <= num3:
	print num1
if num1 >= num2 or num2 >= num3:
	print num2
else:
	print num3



# qus 10
marks = [[45, 21, 42, 63], [12, 42, 42, 53]]
i = 0
small_list = len(marks[i])
while i < marks:
	small_list = len(marks[i])
	j = 0
	while i < small_list:
		print small_list[i][j]
		i = i + 1
j = j + 1
	
	
	

