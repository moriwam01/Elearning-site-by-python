import Read_elearning_Excel_Sheet
import Write_elearning_Excel_Sheet

	
def ClassIndexInteachersDataBase (student_ID) :
	for i in teachers_DataBase :
		for j in teachers_DataBase[i] :							
			if str(student_ID) == str(j[0]) :
				Class_index = teachers_DataBase[i].index(j)
				return Class_index,i

print("********************************************************************")
print("*                                                                  *")
print("*             Welcome to elearning Management                      *")
print("*                                                                  *")
print("********************************************************************")
	
	
tries = 0
tries_flag = ""
while tries_flag != "Close the program" :

		students_DataBase = Read_elearning_Excel_Sheet.Read_students_DataBase()
		teachers_DataBase  = Read_elearning_Excel_Sheet.Read_teachers_DataBase()
				
		print("-----------------------------------------")
		print("|Enter 1 for Administration mode			|\n|Enter 2 for Student mode			|")
		print("-----------------------------------------")
		Administration_Student_mode = input("Enter your mode : ") 
		

		if Administration_Student_mode == "1" :																			#Administration mode
				print("*****************************************\n|         Welcome to Administration mode         |\n*****************************************")
				Password = input("Please enter your password : ")
				while True :
					
					if Password == "anything" :
						print("-----------------------------------------")
						print("|To manage students Enter 1 		|\n|To manage teachers Enter 2	 	|\n|To manage Classs Enter 3 	|\n|To be back Enter E			|")
						print("-----------------------------------------")
						AdministrationOptions = input ("Enter your choice : ")
						AdministrationOptions = AdministrationOptions.upper()
						
						if AdministrationOptions == "1" :															#Administration mode --> students Management
								print("-----------------------------------------")
								print("|To add new student Enter 1	  	|")
								print("|To display student Enter 2	  	|")
								print("|To delete student data Enter 3		|")
								print("|To edit student data Enter 4    	|")
								print("|To Back enter E      			|")
								print("-----------------------------------------")
								Administration_choice = input ("Enter your choice : ")
								Administration_choice = Administration_choice.upper()
								
								if Administration_choice == "1" : 										#Administration mode --> students Management --> Enter new student data
											try :		#Must enter integer input
												student_ID = int(input("Enter student ID : "))
												while student_ID in students_DataBase :		#if Administration entered used ID
													student_ID = int(input("This ID is unavailable, please try another ID : "))					
												Department=input("Enter student department                : ")
												teacherName=input("Enter name of teacher for this subject : ")
												Name      =input("Enter student name                      : ")
												Age       =input("Enter student roll                       : ")
												Gender    =input("Enter student batch                    : ")
												Address   =input("Enter student department                   : ")
												RoomNumber=input("Enter student class number               : ")
												students_DataBase[student_ID]=[Department,teacherName,Name,Age,Gender,Address,RoomNumber]
												print("----------------------student added successfully----------------------")
											except :
												print("student ID should be an integer number")
										
								elif Administration_choice == "2" :										#Administration mode --> students Management --> Display student data
											try :		#To avoid non integer input
												student_ID = int(input("Enter student ID : "))
												while student_ID not in students_DataBase :
													student_ID = int(input("Incorrect ID, Please Enter student ID : "))
												print("\nstudent name        : ",students_DataBase[student_ID][2])
												print("student roll         : ",students_DataBase[student_ID][3])
												print("student batch      : ",students_DataBase[student_ID][4])
												print("student department     : ",students_DataBase[student_ID][5])
												print("student class number : ",students_DataBase[student_ID][6])
												print("student is in "+students_DataBase[student_ID][0]+" department")
												print("student is followed by teacher : "+students_DataBase[student_ID][1])
											except :
												print("student ID should be an integer number")
								
								elif Administration_choice == "3" :										#Administration mode --> students Management --> Delete student data
											try :		#To avoid non integer input
												student_ID = int(input("Enter student ID : "))
												while student_ID not in students_DataBase :
													student_ID = int(input("Incorrect ID, Please Enter student ID : "))
												students_DataBase.pop(student_ID)
												print("----------------------student data deleted successfully----------------------")
											except :
												print("student ID should be an integer number")
										
								elif Administration_choice == "4" :						 				#Administration mode --> students Management --> Edit student data
											try :		#To avoid non integer input
												student_ID=int(input("Enter student ID : "))
												while student_ID not in students_DataBase :
													student_ID = int(input("Incorrect ID, Please Enter student ID : "))
												while True :
													print("------------------------------------------")
													print("|To Edit student Department Enter 1 :    |")
													print("|To Edit teacher following case Enter 2 : |")
													print("|To Edit student Name Enter 3 :          |")
													print("|To Edit student roll Enter 4 :           |")
													print("|To Edit student batch Enter 5 :        |")
													print("|To Edit student department Enter 6 :       |")
													print("|To Edit student RoomNumber Enter 7 :    |")
													print("|To be Back Enter E                      |")
													print("-----------------------------------------")
													Administration_choice = input("Enter your choice : ")
													Administration_choice = Administration_choice.upper()
													if Administration_choice == "1" :
														students_DataBase[student_ID][0]=input("\nEnter student department : ")
														print("----------------------student Department edited successfully----------------------")
														
													elif Administration_choice == "2" :
														students_DataBase[student_ID][1]=input("\nEnter teacher follouing case : ")
														print("----------------------teacher follouing case edited successfully----------------------")
										
													elif Administration_choice == "3" :
														students_DataBase[student_ID][2]=input("\nEnter student name : ")
														print("----------------------student name edited successfully----------------------")
													
													elif Administration_choice == "4" :
														students_DataBase[student_ID][3]=input("\nEnter student roll : ")
														print("----------------------student roll edited successfully----------------------")
												
													elif Administration_choice == "5" :
														students_DataBase[student_ID][4]=input("\nEnter student batch : ")
														print("----------------------student department gender successfully----------------------")
														
													elif Administration_choice == "6" :
														students_DataBase[student_ID][5]=input("\nEnter student department : ")
														print("----------------------student department edited successfully----------------------")
														
													elif Administration_choice == "7" :
														students_DataBase[student_ID][6]=input("\nEnter student RoomNumber : ")
														print("----------------------student class number edited successfully----------------------")
												
													elif Administration_choice == "E" :
														break
														
													else :
														print("Please Enter a correct choice")
											except :
												print("student ID should be an integer number")
																				
								elif Administration_choice == "E" :										#Administration mode --> students Management --> Back
											break
								
								else :
											print("Please enter a correct choice\n")
											
						elif AdministrationOptions == "2" :															#Administration mode --> teachers Management
							print("-----------------------------------------")
							print("|To add new teacher Enter 1              |")
							print("|To display teacher Enter 2              |")
							print("|To delete teacher data Enter 3          |")
							print("|To edit teacher data Enter 4            |")
							print("|To be back enter E                     |")
							print("-----------------------------------------")
							Administration_choice = input ("Enter your choice : ")
							Administration_choice = Administration_choice.upper()
							
							if Administration_choice == "1" : 											#Administration mode --> teachers Management --> Enter new teacher data
									try :		#To avoid non integer input
										teacher_ID = int(input("Enter teacher ID : "))
										while teacher_ID in teachers_DataBase :			#if Administration entered used ID
											teacher_ID = int(input("This ID is unavailable, please try another ID : "))
										
										Department=input("Enter teacher department : ")
										Name      =input("Enter teacher name       : ")
										Address   =input("Enter teacher address    : ")
										teachers_DataBase[teacher_ID]=[[Department,Name,Address]]
										print("----------------------teacher added successfully----------------------")
									except :
										print("teacher ID should be an integer number")
								
							elif Administration_choice == "2" : 											#Administration mode --> teachers Management --> Display teacher data
									try :		#To avoid non integer input
										teacher_ID = int(input("Enter teacher ID : "))
										while teacher_ID not in teachers_DataBase :
											teacher_ID = int(input("Incorrect ID, Please Enter teacher ID : "))
										print("teacher name    : ",teachers_DataBase[teacher_ID][0][1])
										print("teacher address : ",teachers_DataBase[teacher_ID][0][2])
										print("teacher is in "+teachers_DataBase[teacher_ID][0][0]+" department")
									except :
										print("teacher ID should be an integer number")
							
							elif Administration_choice == "3" :											#Administration mode --> teachers Management --> Delete teacher data
									try :		#To avoid non integer input
										teacher_ID = int(input("Enter teacher ID : "))
										while teacher_ID not in teachers_DataBase :
											teacher_ID = int(input("Incorrect ID, Please Enter teacher ID : "))
										teachers_DataBase.pop(teacher_ID)
										print("/----------------------teacher data deleted successfully----------------------/")
									except :
										print("teacher ID should be an integer number")

							elif Administration_choice == "4" :											#Administration mode --> teachers Management --> Edit teacher data
									try :		#To avoid non integer input	
										teacher_ID=input("Enter teacher ID : ")
										while teacher_ID not in teachers_DataBase :
											teacher_ID = int(input("Incorrect ID, Please Enter teacher ID : "))
										print("-----------------------------------------")
										print("|To Edit teacher's department Enter 1    |")
										print("|To Edit teacher's name Enter 2          |")
										print("|To Edit teacher's address Enter 3       |")
										print("To be Back Enter E                      |")
										print("-----------------------------------------")
										Administration_choice=input("Enter your choice : ")
										Administration_choice = Administration_choice.upper()
										if Administration_choice == "1" :
											teachers_DataBase[teacher_ID][0][0]=input("Enter teacher's Department : ")
											print("/----------------------teacher's department edited successfully----------------------/")
											
										elif Administration_choice == "2" :
											teachers_DataBase[teacher_ID][0][1]=input("Enter teacher's Name : ")
											print("----------------------teacher's name edited successfully----------------------")
											
										elif Administration_choice == "3" :
											teachers_DataBase[teacher_ID][0][2]=input("Enter teacher's Address : ")
											print("----------------------teacher's address edited successfully----------------------")
										
										elif Administration_choice == "E" :
											break
										
										else :
											print("\nPlease enter a correct choice\n")
											
									except :
										print("teacher ID should be an integer number")
											
							elif Administration_choice == "E" :											#Back
										break
									
							else :
								print("\nPlease enter a correct choice\n")
											
						elif AdministrationOptions == "3" :															#Administration mode --> Class Management
							print("-----------------------------------------")
							print("|To book an Class Enter 1         |")
							print("|To edit an Class Enter 2         |")
							print("|To cancel an Class Enter 3       |")
							print("|To be back enter E                     |")
							print("-----------------------------------------")
							Administration_choice = input ("Enter your choice : ")
							Administration_choice = Administration_choice.upper()
							if Administration_choice == "1" :												#Administration mode --> Class Management --> Book an Class							
								try :		#To avoid non integer input
										teacher_ID = int(input("Enter the ID of teacher : "))
										while teacher_ID not in teachers_DataBase :
											teacher_ID = int(input("teacher ID incorrect, Please enter a correct teacher ID : "))
										print("---------------------------------------------------------")
										print("|For book an Class for an exist student Enter 1   |\n|For book an Class for a new student Enter 2      |\n|To be Back Enter E                                     |")
										print("---------------------------------------------------------")
										Administration_choice = input ("Enter your choice : ")
										Administration_choice = Administration_choice.upper()
										if Administration_choice == "1" :
												student_ID = int(input("Enter student ID : "))
												while student_ID not in students_DataBase :		#if Administration entered incorrect ID
													student_ID = int(input("Incorrect ID, please Enter a correct student ID : "))	
										
											
										elif Administration_choice == "2" :
											student_ID = int(input("Enter student ID : "))
											while student_ID in students_DataBase :		#if Administration entered used ID
												student_ID = int(input("This ID is unavailable, please try another ID : "))					
											Department=teachers_DataBase[teacher_ID][0][0]
											teacherName=teachers_DataBase[teacher_ID][0][1]
											Name      =input("Enter student name    : ")
											Age       =input("Enter student roll     : ")
											Gender    =input("Enter student batch  : ")
											Address   =input("Enter student department : ")
											RoomNumber=""
											students_DataBase[student_ID]=[Department,teacherName,Name,Age,Gender,Address,RoomNumber]
										
										elif Administration_choice == "E" :
											break
											
										Session_Start = input("Session starts at : ")
										while Session_Start[ :2] == "11" or Session_Start[ :2] == "12" :
											Session_Start = input("Classs should be between 01:00PM to 10:00PM, Please enter a time between working hours : ")
											
										for i in teachers_DataBase[teacher_ID] :
											if type(i[0])!=str :
												while Session_Start >= i[1] and Session_Start < i[2] :
													Session_Start = input("This Class is already booked, Please Enter an other time for start of session : ")
										Session_End   = input("Session ends at : ")
										
										New_Class=list()
										New_Class.append(student_ID)
										New_Class.append(Session_Start)
										New_Class.append(Session_End)
										teachers_DataBase[teacher_ID].append(New_Class)								
										print("/----------------------Class booked successfully----------------------/")
								except :
										print("teacher ID should be an integer number")
					
							elif Administration_choice == "2" :												#Administration mode --> Class Management --> Edit an Class
									try :		#To avoid non integer input
										student_ID = int(input("Enter student ID : "))						
										while student_ID not in students_DataBase :
											student_ID = int(input("Incorrect Id, Please Enter correct student ID : "))
										try :   #To avoid no return function
												ClassIndex,PairKey = ClassIndexInteachersDataBase(student_ID)
												Session_Start = input ("Please enter the new start time : ")
												while Session_Start[ :2] == "11" or Session_Start[ :2] == "12" :
													Session_Start = input("Classs should be between 01:00PM to 10:00PM, Please enter a time between working hours : ")
													
												for i in teachers_DataBase[teacher_ID] :
													if type(i[0])!=str :
														while Session_Start >= i[1] and Session_Start < i[2] :
															Session_Start = input("This Class is already booked, Please Enter an other time for start of session : ")
												Session_End = input ("Please enter the new end time : ")
												teachers_DataBase[PairKey][ClassIndex]=[student_ID,Session_Start,Session_End]							
												print("/----------------------Class edited successfully----------------------/")
										except :
												print("No Class for this student")
									except :
										print("teacher ID should be an integer number")
						
							elif Administration_choice == "3" :												#Administration mode --> Class Management --> Cancel a Class
									try :		#To avoid non integer input
										student_ID = int(input("Enter student ID : "))
										while student_ID not in students_DataBase :
											student_ID = int(input("Invorrect ID, Enter student ID : "))
										try :
												ClassIndex,PairKey = ClassIndexInteachersDataBase(student_ID)						
												teachers_DataBase[PairKey].pop(ClassIndex)
												print("/----------------------Class canceled successfully----------------------/")
										except :
												print("No Class for this student")
									except :	 #To avoid no return function
										print("student ID should be an integer number")
							
							elif Administration_choice == "E" :												#Back
										break
							
							else :
										print("please enter a correct choice")
						
						elif AdministrationOptions == "E" :		                                        	#Back
							break
						
						else :
							print("Please enter a correct option")
					
				
					elif Password != "anything" :
						if tries < 2 :
							Password = input("Password incorrect, please try again : ")
							tries += 1
						else :
							print("Incorrect password, no more tries")
							tries_flag = "Close the program"
							break
				
					Write_elearning_Excel_Sheet.Write_students_DataBase(students_DataBase)
					Write_elearning_Excel_Sheet.Write_teachers_DataBase(teachers_DataBase)
					
					
		elif Administration_Student_mode == "2" :																		#Student mode
			print("****************************************\n|         Welcome to Student mode         |\n****************************************")
			while True :
				print("\n-----------------------------------------")
				print("|To view elearning's departments Enter 1 |")
				print("|To view elearning's teachers Enter 2     |")
				print("|To view students' residents Enter 3    |")
				print("|To view student's details Enter 4      |")
				print("|To view teacher's Classs Enter 5  |")
				print("|To be Back Enter E                     |")
				print("-----------------------------------------")
				StudentOptions = input("Enter your choice : ")
				StudentOptions = StudentOptions.upper()
				
				if   StudentOptions == "1" :											#Student mode --> view elearning's departments
							print("elearning's departments :")
							for i in teachers_DataBase :
								print("	"+teachers_DataBase[i][0][0])
					
				elif StudentOptions == "2" :											#Student mode --> view elearning's teachers
							print("elearning's teachers :")
							for i in teachers_DataBase :
								print("	"+teachers_DataBase[i][0][1]+" in "+teachers_DataBase[i][0][0]+" department, from "+teachers_DataBase[i][0][2])
								
				elif StudentOptions == "3" :											#Student mode --> view students' residents
					for i in students_DataBase :
						print("	student : "+students_DataBase[i][2]+" in "+students_DataBase[i][0]+" department and followed by "+students_DataBase[i][1]+", age : "+students_DataBase[i][3]+", from : "+students_DataBase[i][5]+", RoomNumber : "+students_DataBase[i][6])
				
				elif StudentOptions == "4" :											#Student mode --> view student's details
					try :				#To avoid non integer input
						student_ID = int(input("Enter student's ID : "))
						while student_ID not in students_DataBase :
							student_ID = int(input("Incorrect Id, Please enter student ID : "))
						print("	student name        : ",students_DataBase[student_ID][2])
						print("	student roll         : ",students_DataBase[student_ID][3])
						print("	student batch      : ",students_DataBase[student_ID][4])
						print("	student department     : ",students_DataBase[student_ID][5])
						print("	student class number : ",students_DataBase[student_ID][6])
						print("	student is in "+students_DataBase[student_ID][0]+" department")
						print("	student is followed by teacher : "+students_DataBase[student_ID][1])
					except :
						print("student ID should be an integer number")
							
				elif StudentOptions == "5" :											#Student mode --> view teacher's Classs
					try :				#To avoid non integer input
						teacher_ID = int(input("Enter teacher's ID : "))
						while teacher_ID not in teachers_DataBase :
							teacher_ID = int(input("Incorrect Id, Please enter teacher ID : "))
						print(teachers_DataBase[teacher_ID][0][1]+" has Classs :")
						for i in teachers_DataBase[teacher_ID] :
							if type(i[0])==str :
								continue
							else :
								print("	from : "+i[1]+"    to : "+i[2])
					except :
						print("teacher ID should be an integer number")
					
				elif StudentOptions == "E" :											#Back
					break
					
				else :
					print("Please Enter a correct choice")
					
					
		else :
			print("Please choice just 1 or 2")
