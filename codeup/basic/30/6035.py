"""
[기초-산술연산] 실수 2개 입력받아 곱 계산하기(설명)(py)
------

실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

예시
...
m = f1 * f2
print(m)

참고
수 * 수는 곱(multiplication)이 계산된다.
"""

a, b = input().split()
m = float(a) * float(b)
print(m)