#program to find the given number is prime or not.
num=int(input("Enter a number:"))
flag=False
if(num >1):
    for x in range(2,num):
        if(num%x==0):
            flag=True
            break

if flag:
    print("the number is not a prime.")
else:
     print("The number is prime.")
