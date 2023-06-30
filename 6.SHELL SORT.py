list=[14,48,51,2,96,4,36,7,88]
print(list) 
n=len(list)
gap=int(n/2)
while gap>0:
    for i in range(gap,n):
        key=list[i]
        j=i-gap
        while j>=0 and key<list[j]:
            list[j+gap]=list[j]
            j=j-gap
        list[j+gap]=key
    gap=int(gap/2)
print(list)

9