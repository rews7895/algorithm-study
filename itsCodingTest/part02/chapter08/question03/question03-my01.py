width = 3

result = [0] * (width + 1)

# 처음에는 경우의 수가 1개
result[1] = 1
# 두 번째 부터는 모든 경우의 수가 가능하므로 3
result[2] = 3

for i in range(3, width + 1):
    # 이전 길이에서의 경우의 수와 이전 이전에서의 경우의 수(*2)
    result[i] = (result[i - 1] + (result[i - 2] * 2)) % 796796

print(result[width])