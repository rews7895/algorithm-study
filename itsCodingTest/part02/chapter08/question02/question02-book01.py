# 정수 n을 입력받기
n = int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    # d[i - 1]이 max로 선정된 경우 현상 max값 유지가 되는 것이고
    # d[i - 2] + array[i]가 max로 선정 되었을 경우 현재 바라보는 식량창고를 털 수 있음
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n - 1])