nums = map(int, input().split())

arr=[0]*6
for n in nums:
    arr[n-1]+=1

for i in range(6):
    print(str(i+1)+" - "+str(arr[i]))