from collections import deque

# col, row = map(int, input().split())
#
# li = []
# for y in range(col):
#     li.append(list(map(int, input())))

col, row = 5, 6

li = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]


def bfs(y, x):
    y -= 1
    x -= 1
    queue = deque()
    queue.append((y, x))
    while queue:
        # 가장 처음 값 빼기
        pop_y, pop_x = queue.popleft()
        # 최종적인 출구는 (n, m) 이기 때문에 if문을 오른쪽 -> 아래 -> 위 -> 왼쪽 순으로 정렬
        if 0 <= pop_x + 1 < row and li[pop_y][pop_x + 1] == 1:
            # 이동하며 값을 추가해야 하기 때문에 기존 값 + 1로 설정한다.
            # 이 때 기존 0, 0은 출구가 아니기 때문에 아랫방향 이동 후 위를 체크할 때 갱신되는 값은 무시
            li[pop_y][pop_x + 1] = li[pop_y][pop_x] + 1
            # 다 돌기 전에 최종 출구를 찾았다면 break / 아니면 이동한 값을 다시 큐에 넣는다
            if pop_y == col - 1 and pop_x + 1 == row - 1:
                break
            else:
                queue.append((pop_y, pop_x + 1))
        if 0 <= pop_y + 1 < col and li[pop_y + 1][pop_x] == 1:
            li[pop_y + 1][pop_x] = li[pop_y][pop_x] + 1
            if pop_y + 1 == col - 1 and pop_x == row - 1:
                break
            else:
                queue.append((pop_y + 1, pop_x))
        if 0 <= pop_y - 1 < col and li[pop_y - 1][pop_x] == 1:
            li[pop_y - 1][pop_x] = li[pop_y][pop_x] + 1
            if pop_y - 1 == col - 1 and pop_x == row - 1:
                break
            else:
                queue.append((pop_y - 1, pop_x))
        if 0 <= pop_x - 1 < row and li[pop_y][pop_x - 1] == 1:
            li[pop_y][pop_x - 1] = li[pop_y][pop_x] + 1
            if pop_y == col - 1 and pop_x - 1 == row - 1:
                break
            else:
                queue.append((pop_y, pop_x - 1))

    # 최종적으로 출구의 값을 출력하여 몇번째에 도달했는지 확인한다.
    return li[col - 1][row - 1]


print(bfs(1, 1))

for row in li:
    for x in row:
        print(x, end=' ')
    print()
