#program to print the prime numbers in a given range.
min=int(input("Enter a minimum limit:"))
max=int(input("Enter a maximum limit:"))
for num in range(min,max+1):
    if(num>1):
        for x in range(2,num):
            if(num%x)==0:
                 break
        else:
            print(num)

