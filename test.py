def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(n1):
        L[i] = arr[p + i]
    L[n1] = 2345678

    print(L)

    for i in range(n2):
        R[i] = arr[q + 1 + i]
    R[n2] = 2345678
    
    print(R)

arr=[12,45,3,6,34,7,6]
p=0
r=len(arr)-1
q=(p+r)//2
merge(arr,p,q,r)

