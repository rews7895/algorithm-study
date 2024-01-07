n = 2
m = 15
# 화폐 단위
units = [2, 3]

# 키는 화폐 크기 / 값은 최소 화폐로 개수
# 화폐를 하나도 사용하지 않을 경우 0을 만들 수 있기 때문에 시작은 0
result = [0] + ([10001] * m)

for i in range(n):
    for j in range(units[i], m + 1):
        if result[j - units[i]] != 10001:
            result[j] = min(result[j], result[j - units[i]] + 1)

print(result[m])
