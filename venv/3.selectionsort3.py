def selectionsort(list,n):
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if(list[j]<list[min]):
                min=j
        temp=list[min]
        list[min]=list[i]
        list[i]=temp
    print(list)
list=[3,6,5,1,2,0,4]
selectionsort(list,len(list))
