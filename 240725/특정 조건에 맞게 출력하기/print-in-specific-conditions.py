numbers = map(int, input().split())

for i in numbers:
    if i==0:
        break
    if i%2==1:
        print(i+3, end=" ")
    else:
        print(i//2, end=" ")