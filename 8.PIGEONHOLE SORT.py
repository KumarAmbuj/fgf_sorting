def pigeonholesort(arr):

    max1=max(arr)
    min1=min(arr)
    size=max1-min1+1
    count=[0]*size

    for i in range(len(arr)):
        count[arr[i]-min1]=count[arr[i]-min1]+1

    output=[]
    for i in range(len(count)):
        while count[i]>0:
            output.append(i+min1)
            count[i]=count[i]-1
    print(output)



a = [8, 3, 2, 7, 4, 6, 8]
pigeonholesort(a)
