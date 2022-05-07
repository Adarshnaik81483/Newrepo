#program to find the given year is leap year or not.
a=int(input("Entr an year:"))
if(a%400==0 and a%100==0):
    print("it is leap year.")
elif(a%4==0 and a%100!=0):
    print("it is leap year")
else:
    print("it is not leap year.")