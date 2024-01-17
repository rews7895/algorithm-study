def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = 7, 12
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for i in [(1, 2, 3), (1, 3, 2), (3, 2, 1), (2, 5, 2), (3, 4, 4), (7, 3, 6), (5, 1, 5), (1, 6, 2), (6, 4, 1), (6, 5, 3), (4, 5, 3), (6, 7, 4)]:
    a, b, cost = i[0], i[1], i[2]
    edges.append((cost, a, b))

edges.sort()

last = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        # 간선 총계
        result += cost
        # 마지막 하나를 끊어서 2개 집합으로 만든다
        last = cost


print(result - last)