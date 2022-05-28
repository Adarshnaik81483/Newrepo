# l=0
# try:
#     a=1/l
# except:
#     print("please find the error")
# else:
#     print(a)
# finally:
#     print("done")

# what is json
'''JSON means javascript object notation, which is derived from the javascript.
json is text based data format which is used to store the data and transfer the data.
the datas are in the form of key, value pair which are separated by the commas,
'''

# # JSON example
# import json
# # print(dir(json))
# data='{"a":"adarsh","b":"akash","c":"arun"}'
# data1=json.loads(data)
# print(data1)

#method overloading.
# from multipledispatch import dispatch
# @dispatch(int,int)
# def product(a, b):
#     p = a * b
#     print(p)
      
# # Second product method
# # Takes three argument and print their
# # product

# @dispatch(int,int,int)
# def product(a, b, c):
#     p = a * b*c
#     print(p)
  
# # Uncommenting the below line shows an error    
# product(4, 5)
  
# # This line will call the second product method
# product(5, 5,2)

# polimorpism.
# class bangalore:
#     def marat(self):
#         print("it is an city")
#     def gor(self):
#         print("sssss")

# class bombay:
#     def marat(self):
#         print("it is not there in bombay.")
#     def gor(self):
#         print("nooooo")

# def pr(obj):
#     obj.marat()
#     obj.gor()
# A=bangalore()
# B=bombay()
# pr(A)
# pr(B)

# polymorpism
# class bangalore:
#     def marat(self):
#         print("it is an city")
#     def gor(self):
#         print("sssss")

# class bombay:
#     def marat(self):
#         print("it is not there in bombay.")
#     def gor(self):
#         print("nooooo")

# A=bangalore()
# B=bombay()
# for x in (A,B):
#     x.marat()
#     x.gor()

#python function treated as object like below,
# def add(a,b):
#     return a+b
# print(add(4,7))
# sr=add
# print(sr(8,7))

#decorator.
# def pr(txt):
#     return txt.upper()

# def sr(txt):
#     return txt.lower()

# def wr(fun):
#     A=fun("hello")
#     print(A)
# wr(pr)
# wr(sr)

#decorator.
# def con1(s):
#     def con2(t):
#         return s+t
#     return con2

# A=con1("adarsh")
# B=A(" Naik")
# print(B)

# 