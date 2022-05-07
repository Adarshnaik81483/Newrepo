#program to count number of occurance in a string.
string=input("enter a string:")
sr=input("enter the character which is to be count:")
count=0
for x in string:
    if x==sr:
        count=count+1
print("number of occurance is:",count)
