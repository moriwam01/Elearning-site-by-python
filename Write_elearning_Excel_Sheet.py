def Write_Students_DataBase (Students_DataBase) :
	myfile = open("Students_DataBase.csv","w")
	for i in Students_DataBase :
		myfile.write(str(i)+";"+Students_DataBase[i][0]+";"+Students_DataBase[i][1]+";"+Students_DataBase[i][2]+";"+Students_DataBase[i][3]+";"+Students_DataBase[i][4]+";"+Students_DataBase[i][5]+";"+Students_DataBase[i][6]+"\n")
	myfile.close()
	
	
	
def Write_Teachers_DataBase (Teachers_DataBase) :
	myfile = open("Teachers_DataBase.csv","w")	
	for i in Teachers_DataBase :
		myfile.write(str(i)+";")
		for j in Teachers_DataBase[i] :
			myfile.write(str(j[0])+";"+j[1]+";"+j[2]+";")
		myfile.write("\n")
	
	myfile.close()