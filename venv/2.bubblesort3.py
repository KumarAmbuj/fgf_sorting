def bubblesort(list,n):
    for i in range(n):
        swapped=0
        for j in range(n-i-1):
            if(list[j]>list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
                swapped=1
        if(swapped==0):
            break;
    print(list)

list=[3,2,1,4,5,33,5,3]
bubblesort(list,len(list))