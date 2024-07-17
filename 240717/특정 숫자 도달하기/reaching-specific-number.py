numlist = list(map(int, input().split()))
total=0
for i in range(0, 10):
    if numlist[i]>=250:
        break
    else:
        total+=numlist[i]

print(total, end=" ")
avr=total/i
print("%0.1f"%avr)