str="avinash avinash jnajvkjsd asdv as dvas v sv a avinash   avinash"
word=input("enter the word")
count=0
for i in str.split():
    if word==i:
        count=count+1
    else :
        continue
print(count)