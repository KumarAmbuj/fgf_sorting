import numpy as np
import random

randnums= np.random.randint(1,101,5)
def partition(arr,p,r):
    pivot=arr[r]
    i=p-1
    for j in range(p,r):
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1
def quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        for i in range(p,q):
            print(arr[i],end=' ')
        print('(',arr[q],')',end=' ')
        for i in range(q+1,r+1):
            print(arr[i],end=' ')
        print()
        quicksort(arr,p,q-1)
        quicksort(arr,q+1,r)

x = random.randint(10,25)
randnums= np.random.randint(10,99,x)
print('Array Elements:')
print(randnums)
print()
print('Sorting.....')
quicksort(randnums,0,len(randnums)-1)
print('Sorted Elements')
print(randnums)




