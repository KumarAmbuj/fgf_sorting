def merge(arr,p,q,r):
    n1=q-p+1
    n2=r-q

    L=[0]*(n1+1)
    R=[0]*(n2+1)

    for i in range(n1):
        L[i]=arr[p+i]
    L[n1]=2345678

    for j in range(n2):
        R[j]=arr[q+1+j]
    R[n2]=2345678

    i=0
    j=0
    for k in range(p,r+1):
        if L[i]<=R[j]:
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
arr=[12,45,3,6,34,7,6,90]
mergesort(arr,0,len(arr)-1)
for i in range(len(arr)):
    print(arr[i],end=' ')

