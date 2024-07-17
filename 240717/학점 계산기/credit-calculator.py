n = int(input())
arr = list(map(float, input().split()))
total = 0
for i in arr:
    total+=i

avr = total/n
print("%0.1f" %avr)
if avr>=4.0:
    print("Perfect")
elif avr>=3.0:
    print("Good")
else:
    print("Poor")