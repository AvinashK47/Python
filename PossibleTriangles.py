s1=int(input("enter the first side  "))
s2=int(input("enter the second side  "))
s3=int(input("enter the third side  "))
if (s1+s2>=s3 and s2+s3>=s1 and s3+s1>=s2):
    print("Possible")
else :
    print("Not Possible")