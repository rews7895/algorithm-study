# 내 풀이

size = int(input())    # n x n 구축을 위한 입력 값
input_list = input().split()

f = {'x': 1, 'y': 1}    # 좌표를 담아 놓을 딕셔너리

for i in range(len(input_list)):
    match input_list[i]:    # match절로 각 상황에 따른 분기
        case 'L':
            if f['x'] > 1:  # 왼쪽의 경우 -1만 체크
                f['x'] -= 1
        case 'R':
            if f['x'] < size:  # 오른쪽의 경우 size 값 체크
                f['x'] += 1
        case 'U':
            if f['y'] > 1:  # 위의 경우 -1만 체크
                f['y'] -= 1
        case 'D':
            if f['y'] < size:  # 아래의 경우 size 값 체크
                f['y'] += 1

            # 하여 범위 내에서만 체크 할 수 있도록 조건 분기 처리

print(f['y'], f['x'])   # 최종 확인
