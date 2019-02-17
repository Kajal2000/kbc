question_list = ["navgurukul me kitne bacche hain?","navgurukul ke co-founder kon hain?","navgurukul kab start hua tha?","navgurukul me kitne councle member hain","Navgurukul ka current Disko kon haiin","Navgurukul ke kitne team member hain","Komal kitne ladki ka naam hain ng me","Ng me kitni Disko hain current me","Mumbai me kab seft ho rahe h"]

first_option = ["54","amar","2014","10","kajal","10","12","2","10th june"]
second_option = ["60","Rishabh","2015","8","Ravina","8","2","1","12 dec"]
third_option = ["40","Shivam","2016","15","Shivani","10","5","5","13 dec"]
fourth_option = ["50","Rahul","2017","6","savita","20","10","10","15dec"]

all_option = [first_option,second_option,third_option,fourth_option]
ans_key = [0,1,2,3,0,2,1,1,3]
rupes = ["1000","2000","5000","1000","15,000","20,000","25,000","30,000","50000",1000]
ans_list = []
serial_number = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < len(question_list):
	print str(question_list[i])+str(len(question_list[i]))
	j = 0
	while j < len(all_option):
		print str(serial_number[j])+"-"+all_option[j][i]
		j = j + 1
	var = int(raw_input("enter your number"))
	#ans_list.append(var)

	if var-1 == ans_key[i]:
		print "Congrats"+str(rupes[i])
	else:
		print "sorry aapka ans glat hain nhi"

	i = i + 1
