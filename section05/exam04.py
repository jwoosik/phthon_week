'''
차량 2부제
차량번호 예시: '237가1234', '서울가1234', '20나1234'
차량 번호 끝자리 숫자를 판단해서 홀수이면 '운행불가' 짝수면 '운행가능'

차량번호를 입력하세요 >>> '237가1234'
차량번호는 237가1234'는 오늘 운행 가능입니다.

문자열 슬라이스, 형변환, 연산, 조건문
'''
'''
num = input('차량번호를 입력하세요 >>> ')

car = int(num[-4:])
res = num % 2
if res:
    print(f'차량번호 {car}은 오늘 운행 불가입니다.')
else:
    print(f'차량번호 {car}은 오늘 운행 가능입니다.')
'''
    
# 문자열 안에서 작은 따옴표나 큰따옴표 넣기
number = '123가1234'
name = f'\'{number}\''
name = f'\"{number}\"'

name = f'"{number}"'
name = f"'{number}'"


num = input('차량번호를 입력하세요 >>> ')

num1 = int( num[-1] )
res = num1 % 2 # 나눈 값이 1이면 True, 0이면 False
result = '운행 불가' if res else '운행 가능'
print(f'차량번호 \'{num}\'는 오늘 {result}입니다.')


