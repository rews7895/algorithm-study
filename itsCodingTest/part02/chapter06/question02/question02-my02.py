# cnt = int(input())

# li = []
# for i in range(cnt):
#     name, score = input().split()
#     li.append({'name': name, 'score': int(score)})
li = [
    {'name': '홍길동', 'score': 95},
    {'name': '이순신', 'score': 77},
]

li = sorted(li, key=lambda dicItem: dicItem['score'])

for dicItem in li:
    print(dicItem['name'], end=' ')
