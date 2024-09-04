# create a class Employee with 5 parameters
# funct to store values for it
# name , salary , designation
# class - student 
# attributes : name, regno, cgpa, semester 
#create 5 objects of students store their attributes

class Employee:
    # name="default"
    # Salary=0000
    # Designation=0
    # Semester = 0
    def __init__(self):
        self.Name=input("Enter the Name of Employee : ")
        self.Salary=int(input("Enter the Salary : "))
        self.Designation=(input("Enter the Deisgnation : "))
    def Details(self):
        print("Name of Employee : ",self.Name)
        print("Salary : ",self.Salary)
        print("Designation : " , self.Designation )
        
# main

Employee1 = Employee()
Employee2 = Employee()
Employee1.Details()
Employee2.Details()