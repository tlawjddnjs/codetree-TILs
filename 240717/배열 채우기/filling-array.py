numlist = list(map(int, input().split()))
finish = 9
for i in range(len(numlist)):
    if numlist[i]==0:
        finish = i-1
    
for n in numlist[finish::-1]:
    print(n, end=" ")