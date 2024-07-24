arr=['L', 'E', 'B', 'R', 'O', 'S']

s = input()
if s in arr:
    for elem in range(6):
        if s==arr[elem]:
            print(elem)
            break
else:
    print("None")