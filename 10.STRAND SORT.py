def strandsort(arr):

    output=[]

    while(len(arr)>0):

        sublist=[]
        sublist.append(arr[0])
        arr.remove(arr[0])

        i=0

        while(i <len(arr)):
            if arr[i]>sublist[-1]:
                sublist.append(arr[i])
                arr.remove(arr[i])
            else:
                i=i+1


        i=0
        while(len(sublist)>0):

            output.insert(0,sublist.pop())

    print(output)
a = [10, 5, 30, 40, 2, 4, 9]
print(a)
strandsort(a)




