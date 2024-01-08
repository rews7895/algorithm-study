input = 5
li = [3, 1, 2, 2, 5]
result = [0] * input

result[0] = li[0]
result[1] = max(result[0], li[1])
for i in range(2, input):
    result[i] = max(result[i - 1], result[i - 2] + li[i])

print(result)
# print(result[input - 1])

