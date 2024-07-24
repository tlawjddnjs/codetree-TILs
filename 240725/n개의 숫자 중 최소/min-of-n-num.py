# 입력 받기
N = int(input())
numbers = list(map(int, input().split()))

# 최솟값 찾기
min_value = min(numbers)

# 최솟값의 개수 세기
min_count = numbers.count(min_value)

# 결과 출력
print(min_value, min_count)