"""
[기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2(py)
------

정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

while 조건식 :
  ...
  ...

반복 실행구조를 사용해 보자.

참고
조건검사, 출력, 감소의 순서와 타이밍을 잘 생각해보자.
"""

i = int(input())
while True:
    i -= 1
    print(i)
    if i == 0:
        break