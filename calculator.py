a=int(input("enter a: "))
b=int(input("enter b: "))
print("1 for add")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
c=int(input("enter the keyword for operations :"))
if(c==1):
    z=a+b
    print("your desired result is :",z)
elif(c==2):
    z=a-b
    print("your desired result is :",z)
elif(c==3):
    z=a*b
    print("your desired result is: ",z)
elif(c==4):
    z=a/b
else:
    print("enter the operator correctly")