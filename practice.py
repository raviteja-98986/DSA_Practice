input=list(map(str,input().split()))
pos=0
res=[]
for ind,i in enumerate(input):
    if i.isalpha():
        window=[ input[j] for j in range(pos,ind+1)]
        window.pop()
        if len(window)!=1:
            window.remove(min(window))
        # print(window)
        pos=ind+1
        res.append(window)
li=[]

for i in res:
    for j in i:
        li.append(j)
print(li)


