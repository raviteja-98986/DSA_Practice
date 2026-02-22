li=[1,2,2,2,1,3,3,4,5]
dict={}
for i in li:
    dict[i]=dict.get(i,0)+1
print(dict)