# 내 풀이

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y = [1, 2, 3, 4, 5, 6, 7, 8]

cnt = 0

i = input()
x_index = x.index(i[0])     # 해당 x 좌표정보 배열의 인덱스 값으로 변경
y_index = y.index(int(i[1]))    # 해당 y 좌표정보 배열의 인덱스 값으로 변경

patterns = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]     # 좌표 경우의 수
for pattern in patterns:
    # 각 경우의 수를 더하거나 빼고
    x_result = x_index + pattern[0]
    y_result = y_index + pattern[1]
    # 결과 값들이 배열 길이 안에 들어올 경우 cnt++
    if 0 <= x_result <= 7 and 0 <= y_result <= 7:
        cnt += 1

print(cnt)
