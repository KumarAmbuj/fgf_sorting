def flip(arr, i):
    start=0

    while(start<i):

        arr[start], arr[i]= arr[i],arr[start]
        i=i-1
        start=start+1

def findmax(arr,end):

    max=0
    for i in range(1,end+1):
        if arr[i]>arr[max]:
            max=i
    return max

def pancakesort(arr):

    currsize=len(arr)-1

    while currsize>1:

        mi=findmax(arr,currsize)

        if mi!=currsize:

            flip(arr,mi)

            flip(arr,currsize)
        currsize=currsize-1
    print(arr)
arr = [23, 10, 20, 11, 12, 6, 7]
pancakesort(arr)

