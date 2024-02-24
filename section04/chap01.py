'''
연산자와 우선순위
'''

'''
산술연산자: +, -, *, /, //(정수의 나누기, 몫만 취함), %(정수의 나누기, 나머지만 취함), **(거듭제곱)
대입연산자: =, +=, -=, *=, /=, //=, %=, **=
total = 0
total = total + number ==> total += number
total = total + 1 ==> total = 2
total = total + 1
total = total + 1
...
관계연산자: >, >=, <, <=, ==, !=
관계연산의 결과는 True(논리값) 또는 False(논리값)로 정해진다.
논리값이 무조건 나오게 됨
False = 5 > 10

논리연산자: and, or, not
논리연산의 결과는 True(논리값) 또는 False(논리값)로 정해진다.
True = True or False

비트연산자: &, |, ^, ~(not 연산), <<, >>, >>>
비트는 0아니면 1로 표현
1바이트는 8비트

기타연산자: 삼항연산자(참 if 논리식 else 거짓), in, +, *
논리식안에 관계식이 포함되어 있음
'''
# 관계연산자를 활용한 방식
# 관계식
print( 5 > 10 ) # 5는 10보다 큰가? 

result = 5 > 10 # 5는 10보다 큰가?
print( result ) # False 출력

result = 5 <= 10 # 5는 10보다 작거나 같은가?
print( result ) # True 출력

result = 5 == 10 # 5는 10이랑 같나?
print( result ) # False 출력
print('======================================')

# 논리 연산
res1 = 5 == 10 # 5는 10이랑 같나? False
res2 = 5 <= 10 # 5는 10보다 작거나 같은가? True
print(res1, res2)

# True/True 이외에는 전부 False
result = res1 and res2 # False and True ===> False
print( result )

# False/False 이외에는 전부 True
result = res1 or res2 # False or True ===> True
print( result )

# not은 하나의 논리값으로. 결과를 반전. True면 False, False면 True로
result = not res2 # not True ===> False
print( result )

# age = int(input('나이를 입력하세요.'))
# age 10보다 크고 18보다 작으면 청소년
# (10 < age) and (age < 18)

# 비트의 연산의 결과는 산술연산과 동일하다.
'''
1byte ===> 8bit
0 ===> 0000 0000
1 ===> 0000 0001
2 ===> 0000 0010
3 ===> 0000 0011
4 ===> 0000 0100
5 ===> 0000 0101
6 ===> 0000 0110
7 ===> 0000 0111
8 ===> 0000 1000

비트연산자: &, |, ^, ~(not 연산), <<, >>, >>>
  0011
& 0100 (and)
=======
  0000
두개의 값 전부 1이여야 1로 계산

  0011
| 0100 (or)
=======
  0111
둘 중 하나라도 1이면 1로 계산

^: Exclusive OR
  0011
^ 0110
=======
  0101
서로 다를 때 1로 계산, 같으면 0

~ 0011 ===> 1100 // True False가 아닌 숫자가 나옴

Shift 연산: 비트를 왼쪽(오른쪽) 방향으로 이동시킨다.

result = 3 << 2 ==> 3을 왼쪽으로 2비트 이동시킨다.
result = 0011 << 2
result = 1100 왼쪽으로 이동시킬 때는 오른쪽에 0이 채워진다.

제일 앞의 값은 부호 비트
1000 0011 << 2 // 제일 앞의 값은 건드리지 않음
result = 1000 1100

>> 부호 유지
>>> 부호 바꾸고 옮김
1001 1000

'''




