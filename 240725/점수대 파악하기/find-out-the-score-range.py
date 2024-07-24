numbers = map(int, input().split())

cnt=[0]*10
for n in numbers:
    if n==0:
        break
    if n<10:
        continue
    cnt[(n//10)-1]+=1

for i in range(9, -1, -1):
    print((i+1)*10, end=" - ")
    print(cnt[i])