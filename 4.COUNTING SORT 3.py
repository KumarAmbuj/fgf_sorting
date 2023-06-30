list=[2,1,1,0,2,5,4,0,2,8,7,7,9,0,1,9]

print(list)

count=[0]*10

for i in range(len(list)):
    count[list[i]]=count[list[i]]+1
for i in range(1,len(count)):
    count[i]=count[i]+count[i-1]
output=[0]*len(list)

for i in range(len(list)-1,-1,-1):
    count[list[i]]=count[list[i]]-1
    output[count[list[i]]]=list[i]
print(output)