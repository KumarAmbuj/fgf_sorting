def selectionsort(list,n):
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if(list[j]<list[min]):
                min=j
        temp=list[i]
        list[i]=list[min]
        list[min]=temp
    print(list)

list=[23,78,45,8,32,5,89]
selectionsort(list,len(list))