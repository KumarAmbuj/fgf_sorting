def insertionsort(a,n):
    for j in range(1,n):
        key=a[j]
        i=j-1
        while(i>=0 and a[i]>key):
            a[i+1]=a[i]
            i=i-1
        a[i+1]=key
    print(a)

list=[1,9,5,3,7,8,4]
insertionsort(list,len(list))