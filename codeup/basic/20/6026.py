"""
[기초-값변환] 실수 2개 입력받아 합 계산하기(설명)(py)
------

실수 2개를 입력받아
합을 출력하는 프로그램을 작성해보자.

참고
입력되는 값은 기본적으로 문자열로 인식된다.

숫자로 구성된 문자열이나 정수를 실수(real number) 값으로 바꾸기 위해서는 float( ) 를 사용할 수 있다.
소숫점(.)은 그 위치가 정해져있지 않고 이리저리 둥둥 떠다니므로, floating point라고 부른다.
"""

a = input()
b = input()
print(float(a) + float(b))