#get duplicate keys is not working
mydict3 = {10:56, 10:4, 20:1, 20:9, 30:1, 50:6}
mydict4 = {}
for x in mydict3:
       if x in mydict4:
              mydict4[x] += 1
       else:
              mydict4[x] = 1
print(mydict4)