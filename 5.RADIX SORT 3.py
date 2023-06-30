def countingsort(arr,exp):
    count=[0]*10
    for i in range(len(arr)):
        count[(arr[i]//exp)%10]=count[(arr[i]//exp)%10]+1

    for i in range(1,len(count)):
        count[i]=count[i]+count[i-1]


    output=[0]*len(arr)

    for i in range(len(arr)-1,-1,-1):
        count[(arr[i]//exp)%10]=count[(arr[i]//exp)%10]-1
        output[count[(arr[i]//exp)%10]]=arr[i]

    for i in range(len(output)):
        arr[i]=output[i]
def radixsort(arr):
    max1=max(arr)

    exp=1

    while (max1//exp)>0:

        countingsort(arr,exp)

        exp=exp*10

arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
radixsort(arr)
for i in range(len(arr)):
    print(arr[i],end=' ')


