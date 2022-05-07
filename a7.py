#program to convert lower case string to upper case string using inbuilt function.
string=input("Enter a lower case string:")
a=string.upper()
print(a)
#program to convert lower case string to upper case string without using inbuilt function.
smp=input("please enter your string:")
smp1=''

for i in smp:
    if(i>='A' and i<='Z'):
        smp1=smp1+chr((ord(i)+32))
    elif i >= 'a' and i <= 'z':
        smp1=smp1+chr((ord(i)-32))
    else:
        pass
print("\noriginal= ",smp)
print("the result= ",smp1)

