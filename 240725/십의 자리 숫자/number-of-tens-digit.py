nums = map(int, input().split())

cnt = [0]*9
for n in nums:
    if n==0:
        break
    if n>=10:
        cnt[(n//10)-1]+=1

for i in range(9):
    print(str(i+1)+" - "+str(cnt[i]))