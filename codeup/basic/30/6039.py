"""
[기초-산술연산] 실수 2개 입력받아 거듭제곱 계산하기(py)
------

실수 2개(f1, f2)를 입력받아
f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.

참고
python 언어에서는 거듭제곱(exponentiation)을 계산하는 연산자(**)를 제공한다.
일반적으로 수학 식에서 거듭제곱을 표현하는 사용하는 서컴플렉스/케릿 기호(^)는 프로그래밍언어에서 다른 의미로 쓰인다.
"""

a, b = input().split()
print(float(a) ** float(b))