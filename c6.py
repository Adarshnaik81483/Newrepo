#proram to access the nested list.
list1=[1,2,3,4,[5,6,7,8,9]]
for x in list1:
    if list1[x]==list():
        print(x)
    else:
        print("no nested list found.")