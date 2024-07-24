n, m = map(int, input().split())
numbers = map(int, input().split())

cnt=0
for num in numbers:
    if num==m:
        cnt+=1

print(cnt)