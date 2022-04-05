def Read_students_DataBase() :

	myfile = open("students_DataBase.csv","r")

	students_Dict = dict()
	student_ID = ""
	Department = ""
	teacher_Name = ""
	student_Name = ""
	student_Roll = ""
	student_Batch = ""
	student_Department = ""
	ClassNumber = ""
	flag = 0
	text = myfile.read()
		
	for i in text :
		if flag == 0 :
						if i != ";" :
							student_ID = student_ID + i
						elif i == ";" :
							flag = 1
							
		elif flag == 1 :
						if i != ";" :
							Department = Department + i
						elif i == ";" :
							flag = 2
							
		elif flag == 2 :
						if i != ";" :
							teacher_Name = teacher_Name + i
						elif i == ";" :
							flag = 3
							
		elif flag == 3 :
						if i != ";" :
							student_Name = student_Name + i
						elif i == ";" :
							flag = 4
							
		elif flag == 4 :
						if i != ";" :
							student_Roll = student_Roll + i
						elif i == ";" :
							flag = 5
							
		elif flag == 5 :
						if i != ";" :
							student_Batch = student_Batch + i
						elif i == ";" :
							flag = 6
							
		elif flag == 6 :
						if i != ";" :
							student_Department = student_Department + i
						elif i == ";" :
							flag = 7
							
		elif flag == 7 :
						if i != "\n" :
							ClassNumber = ClassNumber + i
						elif i == "\n" :
							students_Dict[int(student_ID)]=[Department,teacher_Name,student_Name,student_Roll,student_Batch,student_Department,ClassNumber]
							student_ID = ""
							Department = ""
							teacher_Name = ""
							student_Name = ""
							student_Roll = ""
							student_Batch = ""
							student_Department = ""
							ClassNumber = ""
							flag = 0
							
		
	myfile.close()
	return students_Dict
			
			
			
def Read_teachers_DataBase () :

	myfile = open ("teachers_DataBase.csv","r")

	teachers_Dict = dict()
	teacher_ID = ""
	Department = ""
	teacher_Name = ""
	teacher_Address = ""
	student_ID = ""
	Session_Start = ""
	Session_End = ""
	flag = 0

	
	text = myfile.read()

	while text.count(";;") :
		text=text.replace(";;",";")
	
	for i in text :
		if flag == 0 :
					if i != ";" :
						teacher_ID = teacher_ID + i
					elif i == ";" :
						flag = 1
				
		elif flag == 1 :
					if i != ";" :
						Department = Department + i
					elif i == ";" :
						flag = 2
				
		elif flag == 2 :
					if i != ";" :
						teacher_Name = teacher_Name + i
					elif i == ";" :
						flag = 3
				
		elif flag == 3 :
					if i != ";" :
						teacher_Address = teacher_Address + i
					elif i == ";" :
						flag = 4
						teacher_Data_List = [Department,teacher_Name,teacher_Address]
						teachers_Dict[int(teacher_ID)]=[teacher_Data_List]
						
		elif flag == 4 :
					if i != ";" and i != "\n" :
						student_ID = student_ID + i
					elif i == ";" :
						flag = 5
					elif i == "\n" :
						flag = 0
						teacher_ID = ""
						Department = ""
						teacher_Name = ""
						teacher_Address = ""
						
		elif flag == 5 :
					if i != ";" :
						Session_Start = Session_Start + i
					elif i == ";" :
						flag = 6
		
		elif flag == 6 :
					if i != ";" and i != "\n" :
						Session_End = Session_End + i
					elif i == ";" :
						flag = 4
						Class_List = [int(student_ID),Session_Start,Session_End]	
						teachers_Dict[int(teacher_ID)].append(Class_List)
						student_ID = ""
						Session_Start = ""
						Session_End = ""
					elif i == "\n" :
						flag = 0
						teacher_ID = ""
						Department = ""
						teacher_Name = ""
						teacher_Address = ""

	myfile.close()
	return teachers_Dict