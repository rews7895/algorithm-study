# 내 풀이
# n: 배열의 크기, m: 숫자가 더해지는 횟수, k: 배열의 특정한 인덱스에 해당하는 수가 연속해서 k번 더해질 수 없다
"""
입력 예시
5 8 3
2 4 5 4 6
출력 예시
46
"""
n, m, k = map(int, input().split())
li = list(map(int, input().split()))
li = sorted(li, reverse=True)
tot = 0
limit = 0
for i in range(m):
    if limit >= k:
        tot += li[1]
        limit = 0
    else:
        tot += li[0]
        limit += 1

print(tot)



