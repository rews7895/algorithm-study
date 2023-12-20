n, m = 4, 4
# 내 위치 북쪽
x = 1
y = 1
lotate = 0

li = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]

c = [0, 1, 2, 3]

count = 1
li[x][y] = 1
limit = 0
while True:
    if lotate == 0:         # 북쪽  y -= 1
        if li[x][y - 1] == 0:
            y -= 1
            li[x][y] = 1
            limit = 0
            count += 1
        else:
            limit += 1
    elif lotate == 1:       # 동쪽 x -= 1
        if li[x - 1][y] == 0:
            x -= 1
            li[x][y] = 1
            limit = 0
            count += 1
        else:
            limit += 1
    elif lotate == 2:       # 남쪽 y += 1
        if li[x][y + 1] == 0:
            y += 1
            li[x][y] = 1
            limit = 0
            count += 1
        else:
            limit += 1
    elif lotate == 3:       # 서쪽 x += 1
        if li[x + 1][y] == 0:
            x += 1
            li[x][y] = 1
            limit = 0
            count += 1
        else:
            limit += 1
    lotate = c[lotate - 1]

    # 4방향을 체크
    if limit >= 4:
        # 후진 조건 추가하면 될 듯...
        break