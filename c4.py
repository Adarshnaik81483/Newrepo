#program to print sum of natural numbers upto the limit.
num=int(input("Enter the limit:"))
sum=0
if(num<=0):
    print("zero and negative numbers are not allowed.")
else:
    while(num>0):
        sum=sum+num
        num=num-1
    print(sum)
    