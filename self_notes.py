#class
print("#class")
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
        
A=student('adarsh',24)
print("********************")

#class 
print("#class")
class student:
    @staticmethod
    def __init__(name,age):
        print(name,age)
A=student('adarsh',24)
print("**********************")

#exception handling.
print("#exception handling.")
from ast import Break
from re import I
import sys

randomList=['a',0,2]

for entry in randomList:
    try:
        print("the entry is",entry)
        r=1/int(entry)
        Break
    except:
        print("oops!",sys.exc_info()[0],'occured.')
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)
print("********************")

#sys module
print("#sys module")
import sys
print(dir(sys))
print("********************")

#exception handling.
print("#exception handling.")
mylist=[0,1,2,3]
for li in range(len(mylist)):
    try:
        1/mylist[li]
    except:
        print("it will not support for the given number")
    else:
        print(1/mylist[li])
    finally:
        print("Exit")
print("********************")

#class without init method.
print("#class without init method.")
class student:
    def pr(self,a,b):
        return a+b
A=student()
print(A.pr(10,30))
print("********************")

#class with variable.
print("#class with variable.")
class student:
    a = 10
    b = 30
    def pr(self):
        return self.a+self.b
A=student()
print(A.pr())
print("********************")

# Program to display calendar of the given month and year.
print("# Program to display calendar of the given month and year.")
import calendar
month=7
year=2000
print(calendar.month(year,month))
print("********************")

