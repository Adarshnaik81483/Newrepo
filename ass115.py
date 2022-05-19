#Python Program to Check Leap Year. ex: 2000 is a leap year
from itertools import count
import copy

print("program to find the given year is leap year or not.")
a=int(input("Entr an year:"))
if(a%400==0 and a%100==0):
    print("it is leap year.")
elif(a%4==0 and a%100!=0):
    print("it is leap year")
else:
    print("it is not leap year.")
print("********************")

#Traversing the elements of List: By using while loop:
#print("#Traversing the elements of List: By using while loop:")
#l=[23,66,4,5]
#a=0
#while a<=len(l):
 #   print(x for x in l)
  #  a+=1

#Traversing the elements of List: By using for loop:
print("#Traversing the elements of List: By using for loop:")
l=[23,66,4,5]
for x in l:
    print(x)
print("********************")

#Traversing the elements of List:To display only even numbers:
print("#Traversing the elements of List:To display only even numbers:")
li=[22,4,33,5,66,7]
for x in li:
    if x%2==0:
        print(x)
print("********************")

#Traversing the elements of List:To display elements by index wise(-Ve, +ve):
print("#Traversing the elements of List:To display elements by index wise(-Ve, +ve):")
li=[22,4,33,5,66,7]
a=len(li)
for x in range(a):
    print(li[x])
print("********************")

#Traversing the elements of List:To display elements by index wise(-Ve, +ve):
print("#Traversing the elements of List:To display elements by index wise(-Ve, +ve):")
li=[22,4,33,5,66,7]
a=int(input("Enter the index value:"))
print("the value for the given index is:",li[a])
print("********************")

'''Important functions of List:
I. To get information about list:
1. len():
2. count():
3. index() function:'''
print("Important functions of List:/I. To get information about list:/1. len():/2. count():/3. index() function:")
li=[22,4,33,5,66,7]
a=len(li)
print(a)
li1=["a","a","c","d","s","s","x"]
b=li1.count("a")
print(b)

#index() function:
print("Index is",li1.index("s"))

''' Manipulating elements of List:
1. append() function:
2. insert() function:
Differences between append() and insert()
3. extend() function:
4. remove() function:
5. pop() function:
Differences between remove() and pop()'''
print("append() function.")
l=[2,3]
l.append(4)
print(l)
print("********************")
print("insert() function")
l.insert(1,2)
print(l)
print("********************")
print("Differences between append() and insert() is,\nappend will adds the value to the list after the existing element,\nwhare as insert function will inserts the elements in between the elements by specifying the position.")
print("extend function.")
l1=[5,6,7]
l.extend(l1)
print(l)
print("********************")
print("pop operation")
l.pop()
print(l)
print("********************")
print("remove function")
l.remove(2)
print(l)
print("********************")
#Differences between remove() and pop()
print("Differences between remove() and pop()")
print("pop will delete the end of the list,\n where as remove function will removes the perticular elemets.")
print("********************")

#III. Ordering elements of List:1. reverse():2. sort() function:
print("III. Ordering elements of List:1. reverse(): 2. sort() function:")
#reverse
print("reverse function")
a=[45,3,2,6,66]
a.reverse()
print(a)
print("********************")
#sort function
print("sort function")
a.sort()
print(a)
print("********************")
#Aliasing and Cloning of List objects:1. By using slice operator(using = operater) 2. By using copy() function:
print("#Aliasing and Cloning of List objects:1. By using slice operator(using = operater) 2. By using copy() function:")
print("slicing.")
a=['a','d','a','r','s','h','','n','a','i','k']
c=a[3:9]
print("The sliced elements are:",c)
print("********************")
print("copy function.")
b=[3,2,44,5,4,66]
c=copy.copy(b)
print("copied list is:",c)
c.append(5)
print(c)
print("********************")

#Nested List as Matrix:
print("#Nested List as matrix")
a=[[1,2,3],[4,5,6],[7,8,9]]
for row in a:
    for elem in row:
        print(elem,end=' ')
    print()
print("**********")

#List Comprehensions:
a="jonny jonny yes paaapaaa"
b=a.split()
print(b)
print({x:len(x) for x in b })
print("*******************")

#Write a Python program to convert a given list of tuples to a list of lists.Original list of tuples:
l=[(3,4,5),(1,2,3),(3,2,4)]
for x in l:
    A=print(list(x),end=",")
    B=list(A)
    print(B)










#k=j.split()
#print(k)
#for x in k:
#    a={x:count(m) for m in x}
#print(a)
























