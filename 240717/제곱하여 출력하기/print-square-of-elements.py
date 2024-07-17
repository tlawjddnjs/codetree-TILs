n = int(input())
numbers = list(map(int, input().split()))

numsqr = [i**2 for i in numbers]

for num in numsqr:
    print(num, end=" ")