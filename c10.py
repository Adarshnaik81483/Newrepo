#addition 
#addition 
list1 = [1, 3, 4, 6, 8]
list2 = [4, 5, 6, 2, 10]
list=[]

print("Original list 1 : ",list1)
print("Original list 2 : ",list2)
for i in range(len(list1)):
       list.append(list1[i]+list2[i])
print("the list which is added by list1 and list2:",list)