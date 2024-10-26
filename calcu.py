print("***AREA CALLCULATOR***")
print("""press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of square
press 4 to get the area of square""")

choise=int(input("enter a number between 1-4: "))

if choise==1:
    side=float(input("enter a lenght of one side"))
    area=side**2
    print(" the area of square is ", area)
elif choise==2:  
    length=float(input("enter the length of the rectangle:-") )
    width=float(input("enter the width of the rectangle.."))
    area=length*width
    print("the area of rectangle is ",area)
elif choise==3:
        redius=float(input("enter the radius of the circle"))
        area=(22/7)*(redius**2)
        print("the area of the circle is",area)
        
elif choise==4:
    base=float(input("enter the height of the triangle"))    
    height=float(input("etner the height of the triangle"))    
    area=0.5*base*height
    print("the area of the triangle is ",area)
else:
    print("invalid input")