# qus 1
speed = int(raw_input("enter your number"))
if speed < 30:
	print "Speed bhut kam hai"
elif speed < 60:
	print "Speed kam hai:)"
elif speed > 100:
	print "Speed bahot fast hai"

# qus 2

marks = int(raw_input("enter your number"))
if marks < 25:
    print "fail ho gye"
elif 25 <= 45:
    print "e grad"
elif 45 <= 50:
    print "d grad"
elif 50 <= 60:
    print "c grad"
elif 60 >= 80:
    print "b grad"
elif marks >= 80:
    print "farst ho"
# qus 3

num1 = (raw_input("enter your number"))
num2 = (raw_input("enter your number"))
num3 = (raw_input("enter your number"))
if num1 >= num2:
	largest = num1
elif num2 >= num3:
	largest = num2
else:
	largest = num3

print largest

# qus 4

num1 = (raw_input("enter your number"))
num2 = (raw_input("enter your number"))
num3 = (raw_input("enter your number"))
if num1 <= num2 or num2 <= num3:
	print num1
if num1 >= num2 or num2 >= num3:
	print num2
else:
	print num3

# qus 5

sudent = input("enter your number")
kharcha = input("enter your number")
user = student*kharcha
if user < 50,000:
    print "bagat ke andar hain"
else:
    print "bahar hain"

#if question 6

var = int(raw_input("enter your number :) "))
if var < 10:
	print "10 se chota hai"
elif var > 20 and var < 10:
	print "20 se bada hai"
else:
	print "20 se chota hai"

#if question 7

var = int(raw_input("koi number choose kare :) "))
if var % 2 == 0:
	print "divisible hai"
else:
	print "divisible nhi hai"

#if question 8

var = int(raw_input("koi number le :) "))
if var % 5 and var % 15 == 0:
	print "divisible hai"
else:
	print "divisible nhi hai"
    

 if question 9

age = int(raw_input("enter your age :) "))
if age == 3 and age <= 15:
	print "school jao"
elif age >= 15 and age <= 20:
	print "navgurukul jao"
elif age >= 20 and age <= 25:
	print "job lehlo ok"
elif age >= 25 and age <= 30:
	print "happy :)"
else:
	print "kab ghai ja ok :)"

#if question 10

number1 = input("enter your number")
number2 = input("enter your number")
add=number1+number2
minus=number1-number2
multiply=number1*number2
print add
print minus
print multiply

#  qus 11
year=input("enter the year")
if year%4==0:
	print "it is a leap year"
else:
	print "not a leap year"

# qus 12

number = int(raw_input("chack karo ki :) "))
if number > 99:
	print "100 bada hai"
else:
	print "chota hai"
# qus 13

day = raw_input("Din enter karo\n")
if day == "monday":
	print "Rajma Chawal"
elif day == "tuesday":
	print "Pao Bhaji"
elif day == "wednesday":
	print "Chole Bhature"
elif day == "thursday":
	print "Dosa"
elif day == "friday":
	print "Litti Chokha"
elif day == "saturday":
	print "Thukpa"
else:
	print "Poha"

# qus 14

var1 = int(raw_input("enter your var1 :) "))
var2 = int(raw_input("enter your var2 :) "))
var3 = int(raw_input("enter your var3 :) "))
if var1 < var2:
	print "var2"
elif var2 < var3:
	print "var3"
else:
	print "var1"

# qus 15
user = raw_input("enter your number")
if user in "a,e,i,o,u":
	print "vowel hain",user
else:
	print "nhi h",user
# qus 16
user = raw_input("enter your number")
if user in "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z":
	print "small latter hain"
else:
	print "capital letter hain"

# qus 17
i = 1500
while i < 1700:
	if i % 5 == 0 and i % 7:
		print "disible hain",i
	else:
		print "disible nhi h",i
	i = i + 1
# qus 18
user_1 = raw_input("enter your number")
user_2 = raw_input("enter your number")
if user_1 == user_2:
	print "rectangle"
else:ser
	print "nhi h"

# qus 19

var = raw_input("enter your number")
var1 = raw_input("enter your number")
if var > var1:
	print var
else:
	print var1

# qus 20
var = raw_input("enter your number")
var1 = raw_input("enter your number")
if var > var1:
	print vars
else:
	print var1
# qus 21

year = int(raw_input("enter your number"))
if year % 4 == 0 and year % 400 == 0:
	print "leap year",year
else:
	print "nhi hain",year

# qus 22

num =int(raw_input("enter your number"))
if num % 2 == 0:
    print "even number",num
else:
    print "odd number",num

# qus 23

num = (input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

# qus 24

varx = 300 - 123
user = int(raw_input("enter your number"))
if user == varx:
	print "barab h"
else:
	print "barabar nhi h"

# qus 25

password = raw_input("enter your number")

if len(password) < 6 and len(password) < 16 and "$" in password  and "2"  in password or "8" in password and "A" in password or "z" in password:
	print "strong password h"
else:
	print "nhi h" 

# qus 26

number = int(raw_input("enter your number"))
if number > 18:
	print "eligible hain"
else:
	print "nhi h"

# qus 27


user = raw_input("enter your mecdial report")
if user == "y":
	print "class jao"
else:
	print "nhi jaa skte ho"

# qus 28

i = 1
while i < 10:
	if i % 3 != 0:
		print i
	i = i + 1
# qus 29

a = int(raw_input("enter your number"))
if a == 5:
	print "barabr h"
else:
	print "nhi h"

# qus 30

user = int(raw_input("enter your number"))
if user > 100:
	print "you will get the discount"
cost = user*10/100
print cost
cost_input = user - cost
print cost_input

# qus 31

num1 = int(raw_input("enter your number"))
num2 = raw_input("enter your number")
num3 = raw_input("enter your number")
a=[num1,num2,num3]
print (num2)

# qus 32

i = 1
while i < 50:
	if i % 3 == 0 and i % 5 == 0:
		print str(i)+("-fizzbuzz")
	elif i % 5 == 0:
		print str(i)+("-fizz")
	elif i % 3 == 0:
		print str(i)+("-buzz")
	i = i + 1
print i

# qus 33
#num = raw_input("enter your number")
#print num[:: -1]


# qus 34
user = raw_input("enter your number")
user1 = int(raw_input("enter your number"))
if user == "f":
	print " she will work in urban area"
elif user == "m" and user1 > 20 and user1 < 40:
	print "he will work anywhere"
elif user == "n" and user1 > 40 and user1 < 60:
	print "he will work urban area"
else:
	print "error"

# qus 35


