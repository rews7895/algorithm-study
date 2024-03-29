# 내 풀이
"""
* 방향
    - 0: 북쪽
    - 1: 동쪽
    - 2: 남쪽
    - 3: 서쪽
    
    북
서       동
    남
    
* 맵 속성
    - 0: 육지
    - 1: 바다
"""
"""
1. 먼저 이동할 왼쪽 좌표 확인 후 갈 수 있는 곳이면 이동
2. 방향 변경은 매 턴마다 한번씩 진행
3. 걸었던 길은 2로 바꿈
4. 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 경우 바라보는 방향을 유지한 채로 한칸 뒤로 간다
"""
y, x = map(int, input().split())
col, row, direction = map(int, input().split())
maps = []
for i in range(y):
    maps.append(list(map(int, input().split())))

limit = 0   # 방향 회전 제어 값으로 4가 되면 동, 서, 남, 북 다 돈거다...
maps[col][row] = 2      # 첫 좌표 다녀온 값으로 변경
cnt = 1     # 좌표 이동 회수 (첫 좌표도 포함인듯)

while True:
    match direction:
        case 0:     # 북
            if maps[col - 1][row] == 0:     # 각 좌표별 왼쪽 방향이 육지인지 확인
                col -= 1                    # 맞으면 왼쪽 좌표를 위한 방향 값 변경
                maps[col][row] = 2          # 해당 좌표값 임의 지정한 다녀온 값이라는 2로 변경
                cnt += 1                    # 방문 칸 + 1
                limit = 0                   # 방향 회전 제어 값 초기화
            else:
                limit += 1                  # 방향 회전 제어 값 +1 (3이 되면 모든 방향 다 돈 것)
            direction = 3                   # 방향 값
        case 1:     # 동
            if maps[col][row - 1] == 0:
                row -= 1
                maps[col][row] = 2
                cnt += 1
                limit = 0
            else:
                limit += 1
            direction = 0
        case 2:     # 남
            if maps[col + 1][row] == 0:
                col += 1
                maps[col][row] = 2
                cnt += 1
                limit = 0
            else:
                limit += 1
            direction = 1
        case 3:     # 서
            if maps[col][row + 1] == 0:
                row += 1
                maps[col][row] = 2
                cnt += 1
                limit = 0
            else:
                limit += 1
            direction = 2
    if limit >= 4:  # 후진 조건
        match direction:
            case 0:     # 북
                if maps[col][row + 1] != 0:     # 북의 후방인 남쪽이 바다일 경우 무한 루프 탈출
                    break
                else:
                    row += 1    # 후진
            case 1:
                if maps[col - 1][row] != 0:     # 동의 후방인 서쪽이 바다일 경우 무한 루프 탈출
                    break
                else:
                    col -= 1    # 후진
            case 2:
                if maps[col][row - 1] != 0:     # 남의 후방인 북쪽이 바다일 경우 무한 루프 탈출
                    break
                else:
                    row -= 1    # 후진
            case 3:
                if maps[col + 1][row] != 0:     # 서의 후방인 동쪽이 바다일 경우 무한 루프 탈출
                    break
                else:
                    col += 1    # 후진

print(cnt)

