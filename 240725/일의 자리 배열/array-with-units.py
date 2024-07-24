a, b = map(int, input().split())

arr = []
arr.append(a)
arr.append(b)

for i in range(2, 10):
    num = arr[i-2]+arr[i-1]
    while num>=10:
        num%=10
    arr.append(num)

print(" ".join(map(str, arr)))