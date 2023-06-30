def binarysearch(arr,start,end,val):
    if start==end:
        if arr[start]>val:
            return start
        elif arr[start]<val:
            return start+1

    if start>end:
        return start

    mid=(start+end)//2

    if val<arr[mid]:
        return binarysearch(arr,start,mid-1,val)
    elif val>arr[mid]:
        return binarysearch(arr,mid+1,end,val)
    else:
        return mid

def insertionsort(arr):

    for i in range(1,len(arr)):

        val=arr[i]
        j=i-1
        
        loc=binarysearch(arr,0,i-1,val)

        while(j>=loc):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=val
    print(arr)
arr=[37, 23, 0, 17, 12, 72, 31,46, 100, 88, 54]
insertionsort(arr)