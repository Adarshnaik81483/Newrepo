#remove string from list.
list2 = [{'l':1, 'm':2, 'n':{1:2, 2:{'o':5, 'p':7, "q":'adarsh'}}}]
print(list2[0]['n'][2]["q"])
x = list2[0]['n'][2]["q"]
print({i:x.count(i) for i in x})