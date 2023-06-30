list=[2,1,1,0,2,5,4,0,2,8,7,7,9,0,1,9]
mx=max(list)
mn=min(list)
print(mx)
count=[0]*(mx+1)
for i in range(len(list)):
    count[list[i]]=count[list[i]]+1
print(count)

l=[]
for i in range(len(count)):
    while(count[i]>0):
        l.append(i)
        count[i]=count[i]-1
print(l)