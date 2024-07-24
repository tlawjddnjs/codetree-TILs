# 입력 받기
numbers = list(map(int, input().split()))

# 999나 -999가 나올 때까지의 숫자를 저장할 리스트
valid_numbers = []

# 입력 종료 조건인 999나 -999를 만나기 전까지의 숫자만 저장
for num in numbers:
    if num == 999 or num == -999:
        break
    valid_numbers.append(num)

# 가장 큰 숫자와 가장 작은 숫자 찾기
max_value = max(valid_numbers)
min_value = min(valid_numbers)

# 결과 출력
print(max_value, min_value)