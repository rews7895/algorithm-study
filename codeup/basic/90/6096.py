"""
[기초-리스트] 바둑알 십자 뒤집기(py)
------

부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...

"십(+)자 뒤집기를 해볼까?"하고 생각했다.

십자 뒤집기는
그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후,
다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.

바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

예시
...
for i in range(n) :
  x,y=input().split()
  for j in range(1, 20) :
    if d[j][int(y)]==0 :
      d[j][int(y)]=1
    else :
      d[j][int(y)]=0

    if d[int(x)][j]==0 :
      d[int(x)][j]=1
    else :
      d[int(x)][j]=0
...

참고
리스트가 들어있는 리스트를 만들면?
가로번호, 세로번호를 사용해 2차원 형태의 데이터처럼 쉽게 기록하고 사용할 수 있다.
리스트이름[번호][번호] 형식으로 저장되어있는 값을 읽고 쓸 수 있다.
"""

# b = [[0 for i in range(19)] for j in range(19)]
#
# for i, q in enumerate(b):
#     if i == 9 or i == 11:
#         for y, w in enumerate(q):
#             b[i][y] = 1
#     else:
#         q[9] = 1
#         q[11] = 1

b = []
for i in range(19):
    a = list(map(int, input().split()))
    b.append(a)

i = int(input())
for j in range(i):
    x, y = list(map(int, input().split()))
    for i, j in enumerate(b):
        if i == x - 1:
            for z, k in enumerate(j):
                if k == 0:
                    j[z] = 1
                else:
                    j[z] = 0
        if b[i][y - 1] == 1:
            b[i][y - 1] = 0
        else:
            b[i][y - 1] = 1


for q in b:
    for w in q:
        print(w, end=' ')
    print()