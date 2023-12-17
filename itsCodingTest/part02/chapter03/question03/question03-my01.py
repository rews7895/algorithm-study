# 내 풀이
"""
입력 예시 1
3 3
3 1 2
4 1 4
2 2 2

출력 예시 1
2
------------------------
입력 예시 2
2 4
7 3 1 8
3 3 3 4

출력 예시 2
3
"""
n, m = map(int, input().split())
li = []
max = 0
for i in range(n):
    a = list(map(int, input().split()))
    m = min(a)
    if m >= max:
        max = m

print(max)
