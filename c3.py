#program to print fibonacci series.
num=int(input("Enter a number:"))
fibonacci=0
if(num==0):
    print(0)
elif(num>=1):
    for x in range(1,num+1):
        print("the fibonacci for given input is:",fibonacci)
        fibonacci=fibonacci+x
    
else:
    print("Sorry! fibonacci is not exist for negatives")
