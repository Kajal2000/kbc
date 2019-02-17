# more qus 7
list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
new_list = []
i = 0
while i < len(list1):
	if list1[i] in list2:
		new_list.append(list1[i])
	i = i + 1
print new_list
 
# questions  6

string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh","Divyashish", "Divyashish"]
new_list = []
i = 0
while i < len(string_list):
	if string_list[i] not in new_list:
		new_list.append(string_list[i])
	i = i + 1
print new_list

# question 11

sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system" 
a = sentence.split(" ")
print a

#question 2

a = int(raw_input("enter your number"))
b = int(raw_input("enter your number"))
c = a*b
if c <= 50000:
	print "kharche ke under h"
else:
	print "kharche se bahar hainn" 


