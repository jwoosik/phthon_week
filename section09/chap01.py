'''
내장 함수: 파이썬 기본 패키지에 이미 포함되어서 제공되는 유틸리티(유용한?) 함수들

a = charg(12,3,4,5,6,) # 쉼표로 끝나면 튜플이라고 볼 수 있음

print(1,2,3,4,5) 소괄호는 보통 내장 함수
input() 
int()
float()
len() # len은 길이를 구해주는 함수 기억하기

메소드(Method): 어떤 객체가 제공하는 기능
함수(Function): 파이썬이 기본적으로 제공하는 기능

객체들
list, tuple, set, dict, ''

'{}이나 {}이면'.format(10, 20) # .은 소유의 의미

li = [1,2,3]
# 어떤 객체 안에 소속되어 있는 기능을 메소드라고 함
li.append(10) # li 함수에 10이라는 데이터를 추가

range(1,20) # 생성자
'''

print(chr(97))      # 해당 unicode의 문자를 반환한다 / 아스키코드 10진수의 숫자를 문자로 반환
print(ord('한'))    # 문자를 unicode의 값으로 반환한다.

val = eval('3*4')   # 문자열로 수식을 주면 값을 계산해서 반환한다.
print(val)
val = eval('val+8')
print(val)

# print(format(10000, ','))
# 1_000_000_000 # 숫자 천단위 콤마 표현 방식

str(10) # 주어진 값을 문자열로 반환한다.

# 수학 내장 함수들
# abs() pow() round() sum()
abs(-10)    # 절대값
round(10.5) # 반올림

# 시퀀스에 관련된 내장 함수들
# range()

li = [10, 20, 30, 40, 50]
for tp in enumerate(li):
    print(tp)
    
    
    
li = [5,3,4,2,8,1,9]
li2 = sorted(li) # 오름차순 정렬
print( li2 ) # 정렬한 결과를 내뱉어줌

li = sorted(li, reverse=True) # 내림차순 정렬
print( li )

li = ['현대', '기아', '쌍용']
li2 = [1,2,3,4]
for comp in zip(li, li2): # li, li2 리스트를 묶음
    print(comp)