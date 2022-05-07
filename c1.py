#program to count all characters of string. 
test_str="adarshnaik"
empty_dict={}

for z in test_str:
    if z in empty_dict:
        empty_dict[z]+=1
    else:
        empty_dict[z]=1

print("Count of all characters is:\n",str(empty_dict))

#program to count all characters of string
s=input("Enter any string:")
a={i:s.count(i) for i in s}
print(a)

#program to count all characters of string
sr="adarshnaik"
print(sr[1])


