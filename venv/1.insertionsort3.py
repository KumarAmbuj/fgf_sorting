def insertionsort(list,n):
    for j in range(1,n):
        key=list[j]
        i=j-1
        while(i>=0 and list[i]>key):
            list[i+1]=list[i]
            i=i-1
        list[i+1]=key
    print(list)
list=[1,2,3,1,2,1]
insertionsort(list,len(list))