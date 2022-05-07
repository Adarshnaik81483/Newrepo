#program to find the factorial of a given number.
num=int(input("Enter a number:"))
factorial=1
if(num==0):
    print(0)
elif(num>=1):
    for x in range(2,num+1):
        factorial=factorial*x
    print("the factorial for given input is:",factorial)
else:
    print("Sorry! factorial is not exist for negatives")

