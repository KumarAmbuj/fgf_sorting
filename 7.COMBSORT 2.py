def nextgap(gap):

    gap=(gap*10)//13
    if gap<0:
        return 1
    return gap
def combsort(arr):

    n=len(arr)
    gap=n

    while gap>0 :

        gap=nextgap(gap)

        for i in range(0,n-gap):
            if arr[i]>arr[i+gap]:
                temp=arr[i]
                arr[i]=arr[i+gap]
                arr[i+gap]=temp

    print(arr)
arr = [ 8, 4, 1, 3, -44, 23, -6, 28, 0]
combsort(arr)


