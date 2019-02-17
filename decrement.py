num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
count = 0
con = 0
while i < len(num):
	if num[i] % 2 == 0:
		print "even number",i
		count = count + 1 
	else:
		print "odd number",i 
		con = con + 1
	i = i + 1
print count 
print con


