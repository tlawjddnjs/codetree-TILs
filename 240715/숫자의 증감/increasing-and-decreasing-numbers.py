C, n = input().split()
if C=='A':
    for i in range(1,int(n)+1):
        print(i, end=" ")
else:
    for i in range(int(n),0, -1):
        print(i, end=" ")