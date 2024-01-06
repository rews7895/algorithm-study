input = 3

result = [0] * (input + 1)

# 1을 만들 수 있는 2부터 시작
for i in range(2, input + 1):
    # 가장 효율이 안좋은 순부터 진행해 데이터 덮어 쓰기
    result[i] = result[i - 1] + 1
    if i % 2 == 0:
        # i // 2와 같은 경우 이전 처리 값의 횟수를 먼저 가져온 후 + 1해주면 자기 자신의 회수가 계산 된다
        result[i] = min(result[i], result[i // 2] + 1)
    if i % 3 == 0:
        result[i] = min(result[i], result[i // 3] + 1)
    if i % 5 == 0:
        result[i] = min(result[i], result[i // 5] + 1)

print(result[input])
