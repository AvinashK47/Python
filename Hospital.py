dict={23424:"boy",252534:"girl",3482524592:"girl",143552:"boy",32524545:"girl"}
print(len(dict.keys()))
dict[23872952]="girl"
print(len(dict.keys()))
nb,ng = 0,0
for value in dict.values() :
    if value == "boy" :
        nb=nb+1
    else :
        ng=ng+1
print("Number of boys : ", nb ,"NUmber of girls : ",ng)
CertNo=int(input("Enter the certificate no you want to search : "))
print(dict.get(CertNo,"NOt found"))

KeyList=[]
for key,value in dict.items():
    if value=="girl":
        KeyList.append(key)
    else:
        continue
print(KeyList)