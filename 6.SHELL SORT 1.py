def shellsort(arr):
    n=len(arr)
    gap=len(arr)//2
    while gap>0:

        for i in range(gap,n):
            temp=arr[i]
            j=i-gap

            while(j>=0 and temp<arr[j]):
                arr[j+gap]=arr[j]
                j=j-gap
            arr[j+gap]=temp
        gap=gap//2
    print(arr)
list=[14,48,51,2,96,4,36,7,88]
shellsort(list)


