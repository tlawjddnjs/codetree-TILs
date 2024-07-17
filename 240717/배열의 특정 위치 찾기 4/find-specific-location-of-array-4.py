# 입력을 받습니다. 10개의 정수를 공백으로 구분하여 입력받습니다.
numbers = list(map(int, input().split()))

# 2의 배수의 개수를 셀 변수와 합계를 저장할 변수를 초기화합니다.
count = 0
total_sum = 0

# 주어진 10개의 정수를 순회합니다.
for num in numbers:
    if num == 0:
        break  # 0이 나타나면 반복을 종료합니다.
    if num % 2 == 0:  # 2의 배수인지 확인합니다.
        count += 1
        total_sum += num

# 2의 배수의 개수와 합계를 출력합니다.
print(count, total_sum)