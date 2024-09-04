def LucasNumber(n):
    if n == 0 :
        return 2
    elif n == 1 :
        return 1
    a,b = 2,1
    for i in range (2,n+1):
        c = a + b
        a , b = b , c
    return c

num = LucasNumber(4)
print(num)