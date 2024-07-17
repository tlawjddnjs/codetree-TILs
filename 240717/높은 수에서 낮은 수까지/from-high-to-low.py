a, b=map(int, input().split())
start = max(a, b)
finish = min(a, b)
for i in range(start, finish-1, -1):
    print(i, end=" ")