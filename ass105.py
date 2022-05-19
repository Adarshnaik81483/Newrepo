#write a program to print square of a given number using function.
print("#write a program to print square of a given number using function.")
def sq(n):
    square=n**2
    print(square)
A=sq(3)
print("********")

#Write a function to accept 2 numbers as input and return sum.
print("#Write a function to accept 2 numbers as input and return sum.")
def add(a,b):
    sum=a+b
    return sum
A=print(add(4,5))
print("*********")

#Write a function to check whether the given number is even or odd?
print("#Write a function to check whether the given number is even or odd?")
def eve(a):
    if(a%2==0):
        print("The number is even.")
    else:
        print("the number is odd.")
A=eve(3)
print("*********")

#Write a function to find factorial of given number?
print("#Write a function to find factorial of given number?")
def f(a):
    fact=1
    if(a<0):
        print("factorial is not exist for negative numbers.")
    elif(a==0):
        print("factorial is 0")
    else:
        for x in range(1,a+1):
            fact*=x
        print("factorial is ",fact)
    print("************")
i=int(input("Enter a number:"))
A=f(i)

#program to Returning multiple values from a function
print("#program to Returning multiple values from a f#unction")
def add(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
print(add(4,5))
print("*********")

#Table of the given number.
#program to print mmultiplication table.
print("#program to print mmultiplication table.")
num=int(input("Enter input:"))
for i in range(1,11):
    print(num,"X",i,"=",num*i)
print("**********")

#sum all the numbers in a list
print("#sum all the numbers in a list")
l=[3,4,2,1,3,33,54,43]
sum=0
a=len(l)
for x in l:
    sum+=l[a-1]
    a=a-1
print("The sum for the given list of elements:",sum)
print("**********")

#sum all the numbers in a tuple.
print("#sum all the numbers in a tuple.")
l=(3,4,2,1,3,33,54,43)
sum=0
a=len(l)
for x in l:
    sum+=l[a-1]
    a=a-1
print("The sum for the given list of elements:",sum)
print("**********")

#sum all the numbers in a set
print("#sum all the numbers in a set")
l={3,4,2,1,3,33,54,43}
sum=0
for x in l:
    sum=sum+x
print("The sum for the given list of elements:",sum)
print("************")

#multiply all the numbers in a list.
print("#multiply all the numbers in a list.")
l=[3,4,2,1]
mul=1
for x in l:
    mul=mul*x
print("The multiplication for the given list of elements:",mul)
print("**********")

#multiply all the elements in a tuple.
print("#multiply all the elements in a tuple.")
l=(3,4,2,1)
mul=1
for x in l:
    mul=mul*x
print("The multiplication for the given list of elements:",mul)
print("**********")

#multiply all the elements in a set.
print("#multiply all the elements in a set.")
l={3,4,2,1}
mul=1
for x in l:
    mul=mul*x
print("The multiplication for the given list of elements:",mul)
print("**********")

#program to count all characters of string. 
print("#program to count all characters of string.")
test_str="adarshnaik"
empty_dict={}

for z in test_str:
    if z in empty_dict:
        empty_dict[z]+=1
    else:
        empty_dict[z]=1

print("Count of all characters is:\n",str(empty_dict))
print("**********")

#program to count all characters of string.
print("#program to count all characters of string.")
s=input("Enter any string:")
a={i:s.count(i) for i in s}
print(a)
print("**********")

#Take a list and return a new list with unique elements of the first list.
print("#Take a list and return a new list with unique elements of the first list.")
def fun(li):
    st=set(li)
    return(st)
li=[3,4,2,2,3,6]
print(fun(li))
print("**********")

#program to print pascal triangle for the given numbers.
print("#program to print pascal triangle for the given numbers.")
def pattern(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("12",end="")
        print("\r")
pattern(5) 
print("***************")

#Function to check whether a string is a palindrome or not.
print("#Function to check whether a string is a palindrome or not.")
st="malaya"
if(st==st[::-1]):
    print("The given string is palindrome.")
else:
    print("The given string is not palindrome.")
print("*************")

#Function to check whether a string is a palindrome or not.
print("#Function to check whether a string is a palindrome or not.")
x="malaya"
w=""
for i in x:
    w=i+w

if(x==w):
    print("the string is palindrome.")
else:
    print("the string is not palindrome.")
    
#program to check whether a number is in a given range.
print("#program to check whether a number is in a given range.")
a=range(0,10)
b=int(input("Enter your number to check:"))
if(b in a):
    print(b,"is there in the range of 0 and 10")
else:
    print(b," is not there in the range")
print("**********")
print("**********")
print("**********")
print("**********")