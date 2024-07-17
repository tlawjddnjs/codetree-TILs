numlist = list(map(int, input().split()))
total=0
cnt=0
for i in range(0, 10):
    if numlist[i]>=250:
        break
    else:
        total+=numlist[i]
        cnt=i+1

print(total, end=" ")
avr=total/cnt
print("%0.1f"%avr)