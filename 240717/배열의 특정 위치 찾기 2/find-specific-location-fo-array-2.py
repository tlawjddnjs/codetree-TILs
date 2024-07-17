num = list(map(int, input().split()))
even = num[1::2]
odd = num[0::2]
print(max(sum(even), sum(odd))-min(sum(even), sum(odd)))