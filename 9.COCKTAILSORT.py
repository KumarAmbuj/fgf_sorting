def cocktailsort(arr):
    start=0
    n=len(arr)
    end=n-1
    swapped=True

    while(swapped==True):

        swapped=False

        for i in range(start,end-1):
            if arr[i]>arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
                swapped=True
        if swapped==False:
            break

        swapped=False

        for i in range(end-1,start,-1):
            if arr[i]<arr[i-1]:

                temp=arr[i]
                arr[i]=arr[i-1]
                arr[i-1]=temp
                swapped=True

        start=start+1
        end=end-1
    print(arr)
a = [5, 1, 4, 2, 8, 0, 2]
cocktailsort(a)
