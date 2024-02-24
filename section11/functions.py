'''
사용자 정의 함수

print(), input(), len(), ...

함수 정의: Define a function
함수의 호출: Call a function

매개변수: 함수의 입력값
반환값: 함수의 출력값

매개변수 O, 반환값 O
매개변수 X, 반환값 O
매개변수 O, 반환값 X
매개변수 X, 반환값 X
'''

# 함수의 정의
# 매개변수 O, 반환값 X
# consumer function(method)
def greet(message, count): # 파라미터, 매개변수, 아규먼트(Argument), 인수, 인자 삽입 / 넣지 않아도 가능함
    for n in range(count):
        print(message)

# 매개변수 X, 반환값 X
def say_hello():
    print('안녕하세요, 반갑습니다.')
        
# 매개변수 O, 반환값 O
def add(num1:int, num2:int)->int:
    return num1 + num2  # 함수의 출력값

# 문자열에서 문자의 갯수를 구하는 함수를 만들기
def upper_case(message:str) -> str:
    return message.upper()
    
s = 'abcde'
s.upper()
    
    
# 매개변수 X, 반환값 O
def get_pi():
    return 3.14
        
greet('안녕하세요', 5)  # 생성한 greet 함수를 호출
greet('안녕히계세요', 2)
greet('네네', 3)

num3 = add(10, 20)
num3 = add(3, 7)
num3 = add(1.1, 3.5)
num3 = add(1.1, 3)
num3 = add('안녕하세요', '반갑습니다')