#class example
from ast import Pass
from sre_compile import isstring
from numpy import number
print("#class example")
class student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        print(self.id)
        print(self.name)
A=student(1,"adarsh")
B=A.name="arun"
print(B)
print("********************")

#instance variable,class variable
print("#instance variable,class variable")
class student:
    clg_name="mangalore_university"
    def __init__(self,id,name):
        self.id=id
        self.name=name
        print(self.id)
        print(self.name)
A=student(1,"adarsh")
B=A.name="arun"
print(B)
C=A.clg_name
print(C)
D=student.clg_name
print(D)
print("********************")

#class method
class student:
    counter=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        student.counter=student.counter+1
    def msg(self):
        print(self.name +" got "+self.marks,"%")
    @classmethod
    def object_count(cls):
        return cls.counter
s1=student("adarsh","11")
s2=student("arun","12")
print(s1.msg())
print(student.object_count())
print("*****************")

#class method
class employee:
    number=10
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def pr(cls):
        return cls.number
A=employee("adarsh",33)
print(employee.pr())
print("********************")

#string to int conversion
a="a"
print(a)
b=str(a)
print(b)
print("********************")

#static method
print("#static method")
class sms:
    @staticmethod
    def __init__(name,age):
        print(name)
        print(age)
A=sms("adarsh",44)
print("********************")

#separate character and number from a given string.
s="a5dr61ef"
a=''
b=''
for x in s:
    if x.isdigit():
        a=a+x
    else:
        b=b+x
print(a)
print(b)
v=b+a
n=sorted(v)
print(n)
print("********************")

#dynamic initialization of data to the dictionary.
print("#dynamic initialization of data to the dictionary.")
A=int(input("Enter the limit:"))
z={}
for x in range(A):
    a=input("Enter the name:")
    b=input("Enter the percentage:")
    z[a]=b
print(z)
print("********************")

#deletion of elements from dictionary.
print("#deletion of elements from dictionary.")
d={1:'adarsh',2:'akash',3:'arun',4:'sheela'}
print(d)
del d[2]
print(d)

#Write a program to find the number of occurrences of each letter present in the given string?
print("#Write a program to find the number of occurrences of each letter present in the given string?")
s="adarshnaik"
print({str(x)+" is "+str(s.count(x))+" times, " for x in s})

#
