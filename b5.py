#program to find maximum number within three number.
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if(a>b and a>c):
    print("the maximum number is:",a)
elif(b>a and b>c):
    print("the maximum number is:",b)
else:
    print("the maximum number is:",c)

