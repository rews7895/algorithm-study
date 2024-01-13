# 무한 값 설정
INF = int(1e9)

# 입력 받기
# 노드의 수와 개수 및 간선의 개수를 입력받기
n, m = 5, 7

# k번 회사를 방문한 뒤 x번 회사로 가는 것이 목표
x, k = 4, 5

# 기본 세팅
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신 0으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 입력받은 값 세팅
graph[1][2] = 1
graph[2][1] = 1
graph[1][3] = 1
graph[3][1] = 1
graph[1][4] = 1
graph[4][1] = 1
graph[2][4] = 1
graph[4][2] = 1
graph[3][4] = 1
graph[4][3] = 1
graph[3][5] = 1
graph[5][3] = 1
graph[4][5] = 1
graph[5][4] = 1

# 플로이드 워셜 점화식 수행
for v in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][v] + graph[v][j])

distance = graph[1][k] + graph[k][x]

# 결과 출력
if distance >= INF:
    print(-1)
else:
    print(distance)