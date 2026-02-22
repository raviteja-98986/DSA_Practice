li=[1,2,1,2,3,4,5,3,2,2,1,2]
res=[1,3,5,3]
freq_li=[0]*10
for i in li:
    freq_li[i]=freq_li[i]+i
for i in res:
    print(f"{i}:{li[i]}")