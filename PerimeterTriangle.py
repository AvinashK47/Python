def Triangle_Perimeter (a,b=None,c=None):
    if a and b is None and c is None:
        perimeter=a*3
    elif a and b and c is None :
        perimeter=a*2+b
    else :
        perimeter=a+b+c
    print(perimeter)
print(Triangle_Perimeter(3,4,5))