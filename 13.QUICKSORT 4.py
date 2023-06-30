def partition(arr,p,r):

    pivot=arr[r]
    i=p-1
    
    for j in range(p,r):

        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1
def quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        quicksort(arr,p,q-1)
        quicksort(arr,q+1,r)
arr=[56,34,222,333,111,333,2,555,2,66666,2]
quicksort(arr,0,len(arr)-1)
print(arr)