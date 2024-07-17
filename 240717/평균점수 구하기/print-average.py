score = list(map(float, input().split()))
total = 0

for i in score:
    total += i

print("%0.1f" %(total/8))