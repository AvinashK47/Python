# class - student 
# attributes : name, regno, cgpa, semester 
#create 5 objects of students store their attributes

class Student:
    name="default"
    RegNo=0000
    CGPA=0
    Semester = 0
    def __init__(self):
        name=input("Enter the  name : ")
        RegNo=int(input("Enter the Registration Number : "))
        CGPA=int(input("Enter the CGPA : "))
        Semester=int(input("Enter the Semester:"))
    def Details(self):
        print("NAme : ",self.name)
        print("RegNo : ",self.RegNo)
        print("CGPA : " , self.CGPA )
        print("Semester : " , self.Semester )
        
# main

Student1 = Student()
Student2 = Student()
Student1.Details()
Student2.Details()