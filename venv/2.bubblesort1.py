def bubblesort(list,n):
    for i in range(n):
        swapped=0
        for j in range(n-1-i):
            if(list[j]>list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
                swapped=1
        if(swapped==0):
            break;
    print(list)

list=[3,5,2,6,4,3,1]
bubblesort(list,len(list))
