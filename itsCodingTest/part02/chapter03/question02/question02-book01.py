# 책 풀이 - 단순하게 푸는 답안 예시
# n: 배열의 크기, m: 숫자가 더해지는 횟수, k: 배열의 특정한 인덱스에 해당하는 수가 연속해서 k번 더해질 수 없다
"""
입력 예시
5 8 3
2 4 5 4 6
출력 예시
46
"""
# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력 받은 수들 정렬하기
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 k번 더하기
        if m == 0:  # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:  # m이 0이라면 반복문 탈출
        break
    result += second  # 두 번째로 큰 수를 한 번 더하기
    m -= 1  # 더할 때마다 1씩 빼기

print(result)
