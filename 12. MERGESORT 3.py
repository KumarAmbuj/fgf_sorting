def merge(arr,p,q,r):
    n1=q-p+1
    n2=r-q

    L=[0]*(n1+1)
    R=[0]*(n2+1)

    for i in range(n1):
        L[i]=arr[p+i]
    L[n1]=2345

    for i in range(n2):
        R[i]=arr[q+1+i]
    R[n2]=2345

    i=0
    j=0

    for k in range(p,r+1):

        if L[i]<R[j]:
            arr[k]=L[i]
            i=i+1
        else:
            arr[k]=R[j]
            j=j+1

def mergesort(arr,p,r):

    if p<r:

        q=(p+r)//2

        mergesort(arr,p,q)
        mergesort(arr,q+1,r)
        merge(arr,p,q,r)

arr=[2,4,5,1,6,4,3,88,7,66,5,55,3,23,45,2,11,56,43,44,32,4,11,78]
mergesort(arr,0,len(arr)-1)
print(arr)
