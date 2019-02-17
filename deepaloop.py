# qus 1
i = 5
while i > 0:
    j = 0
    while j < 5:
        print i,
        j = j + 1
    print " "
    i = i - 1
# qus 2

var1 = int(raw_input("enter your number"))
var2 = int(raw_input("enter your number"))
i = 0
sum = 0
while i < var1:
    sum = sum + var2
    i = i + 1
print sum

# qus 3
i = 5
while i > 0:
    print "*" *  i
    i = i -1

# qus 4

i = 10
while i > 5:
    print "*" *  i
    j = 0
    while j < i:
        print j
        j = j + 1
    i = i - 1
# qus 5

i = 0
while i < 100:
    if i % 3 == 0 and i % 7 == 0:
        print "goood",i
    if i % 3 == 0:
        print "happy",i
    if i % 7 == 0:
        print "Awesome",i
    else:
        print "bye",i
    i = i + 1

# qus 6

i = 30 
sum = 0
while i < 420:
	sum = sum + 1
	if sum % 8 == 0:
		print sum
	i = i + 1
# qus 7

x=input("enter your number")
i=0
sum=0
a=0
x_digit=list(str(x))
while i<len(x_digit):
	a=int(x_digit[i])
	sum=sum+a
	i=i+1
if x%sum==0:
	print "harshad number hai",x
else:
	print "harshad number nhi hai",x

# qus 8
num = int(raw_input("enter your number"))
i = 1
while num > 1:
    i = i * num
    num = num - 1
print i

#  qus 9

i = 1
while i < 100:
    if i % 7 == 0:

# qus 10
marks = [[11,2,3], [55,8,9], [44,3,10]]
i = 0
while i < len(marks):
	max = len(marks[i])
    	j = 0
    	num = 0
    	while j < max:
        	if (marks[i][j]) > num:
            		num = marks[i][j]
        	j = j + 1
   	print num
   	i = i + 1

# qus 11

num = [1,2,3,4,5]
i = 0
sum = 0
while i < len(num):
	sum = sum + (num[i])
	i = i + 1
print sum

# qus 12
i = 156
while i < 166:
	a = i - 155
	print a
	i = i + 1

# qus 13
num = [1,2,3,4,5]
i = 0
sum = 0
while i < len(num):
	sum = sum + (num[i])
	i = i + 1
print sum

# qus 14
num = [1,2,3,4,10,11]
i = 0
sum = 0
while i < len(num):
	sum = sum + (num[i])
	i = i + 1
print sum

# qus 15

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

# qus 16

i = 0
while i <= 6:
	if i % 3 != 0:
		print i 
	i = i + 1

# qus 17

first = 0
second = 1
while first < 50:
	print first
	var = first
	first = second
	second = first + var
first = first + 1

# qus 18

i = 0
while i < 9:
	print (str(i)*i)
	i = i + 1
# qus 19
num = int(raw_input("enter yr num"))
i = 2
while i < num:
	if num % i == 0:
		print "prime nhi h",num
		break
	i = i + 1
else:
	print "prime h",num

# qus 20
list = [2,3,4,6,5]
var = 1
i = 0
while i < len(list):
	var = var * (list[i])
	i = i + 1
print (var)
	
# qus 21

num = "1234abcd"
i = 0
var = -1
while i < len(num):
    print (num[var]),
    i = i + 1
    var = var - 1
# qus 22

num = "1234"
i = 0
var = -1
while i < len(num):
    print (num[var]),
    i = i + 1
    var = var - 1
#  qus 23

num = [2,34,5,6,7,2,4,6]
num1 = [3,2,4,6,7]
new = []
i = 0
while i < len(num1):
	if num1[i] in num and num1[i] % 2 == 0:
		new.append(num1[i])
	i = i + 1
print new

# qus 25

num = [2,34,5,6,7,2,4,6]
num1 = [3,2,4,6,7]
new = []
i = 0
while i < len(num1):
	if num1[i] in num and num1[i] % 2 == 0:
		new.append(num1[i])
	i = i + 1
print new

# qus 26

list = [2,3,4,2,3,4,6]
i = 0
new = []
while i < len(list):
	if list[i] not in new:
		new.append(list[i])
	i = i + 1
print new
 # qus 27

list = ["3","5","7","23"]
i = 0
new = []
while i < len(list):
	if list[i] not in new:
		new.append(list[i])
	i = i + 1
print new
# qus 28
list = [2,3,4,5,7,8]
i = 0
sum = 0
while i < len(list):
	sum = sum + list[i]
	i = i + 1
print sum

# qus 29
list = [2,3,4,5,7,8]
i = 0
sum = 0
while i < len(list):
	i = i + 1
print i
# qus 30

list1 = ["red","white","blue","black"]
list2 = ["red","green"]
new = []
i = 0
while i < len(list1):
	if list1[i] not in new:
		new.append(list1[i])
	i = i + 1
print new

# qus 31

i = 146
while i < 156:
	a = i - 145
	i = i + 1
	print a
# qus 32
num = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
count = 0
count1 = 0
i = 0
while i < len(num):
	if num[i] % 2 == 0:
		print "even number hai"
		count = count + 1
	else:
		print "odd number hai"
		count1 = count1 + 1
	i = i + 1
print count
print count1

# qus 33

num = [30,20]
i = 0
sum = 0
while i < len(num):
	sum = sum + num[i]
	i = i + 1
print sum

# qus 34

i = 0
while i < 5:
    print "*" * i
    i = i + 1

# qus 35
i = 5
while i > 0:
    print "*" * i
    i = i - 1
# qus 36
i = 5
while i > 0:
    print "1" * i
    i = i - 1
# qus 37
i = 5
while i > 0:
    print "python" * i
    i = i - 1

# qus 38





