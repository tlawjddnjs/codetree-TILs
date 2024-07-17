arr = list(map(int, input().split()))

even_arr = arr[1::2]
mul3_arr = arr[2::3]
print(sum(even_arr), end=" ")
avr3 = sum(mul3_arr)/3
print("%0.1f" %avr3)