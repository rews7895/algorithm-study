INF = int(1e9)

# 노드의 수와 개수 및 간선의 개수를 입력받기
n, m = 4, 2
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
# A와 B가 서로에게 가는 비용은 1이라고 설정
graph[1][3] = 1
graph[3][1] = 1
graph[2][4] = 1
graph[4][2] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = 3, 4

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
    print(-1)
# 도달할 수 있다면, 최단 거리를 출력
else:
    print(distance)