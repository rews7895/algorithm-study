# col, row = map(int, input().split())
#
#
# li = []
# for y in range(col):
#     li.append(list(map(int, input())))

# col, row = 4, 5
# li = [
#     [0, 0, 1, 1, 0],
#     [0, 0, 0, 1, 1],
#     [1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0],
# ]

col, row = 15, 14
a = [
    '00000111100000',
    '11111101111110',
    '11011101101110',
    '11011101100000',
    '11011111111111',
    '11011111111100',
    '11000000011111',
    '01111111111111',
    '00000000011111',
    '01111111111000',
    '00011111111000',
    '00000001111000',
    '11111111110011',
    '11100011111111',
    '11100011111111',
]
li = []
for y in a:
    li.append(list(map(int, y)))


def dfs(y, x):
    # 탐색할 수 없는 좌표를 확인하여 아니면 탈출
    if not ((0 <= x < row) and (0 <= y < col)):
        return False
    # 얼릴 수 있는 구멍 체크
    if li[y][x] == 0:
        # 구멍은 얼림 처리(1 처리)
        li[y][x] = 1

        # 양 방향 탐색
        dfs(y - 1, x)
        dfs(y + 1, x)
        dfs(y, x - 1)
        dfs(y, x + 1)

        return True
    else:
        return False


result = 0
for y, row_item in enumerate(li):
    for x, value in enumerate(row_item):
        if dfs(y, x):
            result += 1

print(result)

for row in li:
    for x in row:
        print(x, end=' ')
    print()
