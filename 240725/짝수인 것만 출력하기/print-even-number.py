n = int(input())
numbers = map(int, input().split())

for i in numbers:
    if i%2==0:
        print(i, end=" ")