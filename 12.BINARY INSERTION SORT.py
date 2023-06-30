def binarysearch(arr,start,end,val):
    if start==end:
        if arr[start]>val:
            return start
        else:
            return start+1

    if  start>end:
        return start

    mid=(start+end)//2

    if val<arr[mid]:
        return binarysearch(arr,start,mid-1,val)
    return binarysearch(arr,mid+1,end,val)

def insertionsort(arr):
    for i in range(1,len(arr)):
        j=i-1
        val=arr[i]

        loc=binarysearch(arr,0,i-1,val)

        while(j>=loc):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=val
    print(arr)
arr=[37, 23, 0, 17, 12, 72, 31,46, 100, 88, 54]
insertionsort(arr)

