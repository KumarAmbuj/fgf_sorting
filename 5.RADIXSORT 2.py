def radixsort(list):
    exp=1
    mx=max(list)
    while(mx//exp)>0:
        countingsort(list,exp)
        exp=exp*10
def countingsort(list,exp):
    count=[0]*10
    n=len(list)
    for i in range(n):
        count[(list[i]//exp)%10]+=1

    for i in range(1,len(count)):
        count[i]=count[i]+count[i-1]
    output=[0]*n
    for i in range(n-1,-1,-1):
        count[(list[i]//exp)%10]-=1
        output[count[(list[i]//exp)%10]]=list[i]

    for i in range(n):
        list[i]=output[i]





arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
radixsort(arr)
for i in range(len(arr)):
    print(arr[i],end=' ')
