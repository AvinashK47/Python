class Car :
    def Assign(instance):
        instance.Make=input("Enter the Make : ")
        instance.Model=input("Enter the Model : ")
        instance.Colour=input("Enter the Colour : ")
        instance.Engine_Capacity=input("Enter the Engine Capacity : ")
    def display(self):
        print(f"Make : {self.Make} , Model : {self.Model} , Colour : {self.Colour} , Engine Capacity : {self.Engine_Capacity}")
mycar=Car()
mycar.Assign()
mycar.display()