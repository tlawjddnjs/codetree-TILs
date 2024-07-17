n = int(input())
for i in range(n, 101):
    if 90<=i:
        print("A ", end="")
    elif 80<=i:
        print("B ", end="")
    elif 70<=i:
        print("C ", end="")
    elif 60<=i:
        print("D ", end="")
    else:
        print("F ", end="")