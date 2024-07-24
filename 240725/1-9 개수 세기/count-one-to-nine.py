n = int(input())
numbers = map(int, input().split())
cnt=[0]*9

for elem in numbers:
    cnt[elem-1]+=1

print("\n".join(map(str, cnt)))