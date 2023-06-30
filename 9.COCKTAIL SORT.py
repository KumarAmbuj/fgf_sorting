def cocktailsort(arr):

    swapped=True
    n=len(arr)
    end=n-1
    start=0

    while(swapped==True):

        swapped=False

        for i in range(end):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1]=arr[i+1],arr[i]
                swapped=True
        if swapped==False:
            break


        swapped=False

        for i in range(end-1,start,-1):
            if arr[i]<arr[i-1]:
                arr[i], arr[i-1]=arr[i-1],arr[i]
                swapped=True
        end=end-1
        start=start+1
    print(arr)
a = [5, 1, 4, 2, 8, 0, 2]
cocktailsort(a)
