'''
지역변수와 전역변수

함수의 정의(선언)와 호출
'''

# 전역변수
total = 10

def my_func(num1:int):
    print(f'total = {total}')   # 여기서의 total은 전역변수 total이다.
    print(num1)     # 여기서는 num1만 출력

def my_func2():
    global total    # total은 전역변수임을 이 함수안에서 선언한다.
    number = 10     # my_func2의 지역변수
    total = 20      # my_func2의 지역변수로서의 total
    print(total)
    
my_func(2)
my_func2()
print(f'total = {total}')

number = 10
print(f'number = {number}')