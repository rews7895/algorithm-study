"""
[기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기(설명)(py)
------

정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
0 <= a <= 10, 0 <= b <= 10

예시
a = 2
b = 10
print(a << b)  #2^10 = 1024 가 출력된다.

참고
예를 들어 1 3 이 입력되면 1을 2^3(8)배 하여 출력한다.
"""

a, b = input().split()
a = int(a)
b = int(b)
print(a << b)
