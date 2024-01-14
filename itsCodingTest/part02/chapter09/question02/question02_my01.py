import heapq

INF = int(1e9)

n, m, start = 3, 2, 1

information = [[] for i in range(n + 1)]

distance = [INF] * (n + 1)

information[1].append((2, 4))
information[1].append((3, 2))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        current_distance, current_node = heapq.heappop(q)
        if distance[current_node] < current_distance:
            continue

        for i in information[current_node]:
            check_distance = current_distance + i[1]
            if check_distance < distance[i[0]]:
                distance[i[0]] = check_distance
                heapq.heappush(q, (check_distance, i[0]))


dijkstra(start)


total_city = 0
max_hours = 0
for i in distance:
    if i != INF:
        total_city += 1
        max_hours = max(max_hours, i)

print(total_city - 1, max_hours)
