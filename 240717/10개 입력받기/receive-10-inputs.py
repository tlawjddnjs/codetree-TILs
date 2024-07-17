num = list(map(int, input().split()))
total = 0
index = 10

for i in range(len(num)):
    if num[i]==0:
        index=i
        break
    else:
        total+=num[i]

avr = total/index
print(total, end=" ")
print("%0.1f" %avr)