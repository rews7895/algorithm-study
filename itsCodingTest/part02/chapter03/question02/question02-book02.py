# 책 풀이
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

data.sort()  # 입력받은 수 정렬
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)  # 최종 답안 출력