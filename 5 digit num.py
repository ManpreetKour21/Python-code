n=int(input("etnert the num 5 digit "))
if n>=0 and n<=9:
    print("it is single digit number")
elif n>=10 and n<=99:
    print("it is a double digit number..")
elif n>100 and n<999:
    print ("it is a triple digit number..")
elif n>1000 and n<9999:
    print ("it is a for digit number..")
elif n>10000 and n<99999:
    print ("it is a five digit number..")
else:


    print("nothing")    
    