"""
[기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)(py)
------

월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall

예시
...
if n//3==1 :
  print("spring")
...

참고
때때로 수들의 특징을 관찰하고 이용하면 매우 간단히 해결할 수도 있다.
"""
m = int(input())
if m in [12, 1, 2]:
    print('winter')
elif m in [3, 4, 5]:
    print('spring')
elif m in [6, 7, 8]:
    print('summer')
else:
    print('fall')