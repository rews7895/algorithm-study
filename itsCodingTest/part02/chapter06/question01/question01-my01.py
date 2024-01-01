cnt = int(input())
li = []
for i in range(cnt):
    li.append(int(input()))

li = sorted(li, reverse=True)

print(li)