'''
파이썬의 특별한 함수 스타일
'''

# 코드의 생략
def pass_func():
    ... # pass, ... 같은 의미


# 가변 매개 변수
def show(*vals:int, horiz:int=1):
    print(vals)
    for n in vals:
        if horiz == 1:
            print(n, end='\t')
        else:
            print(n)
    print()
    
def greet(message:str, temp:int=2, count:int=3):    # 뒤에 있는 매개변수부터 값을 넣어라
    for n in range(count):
        if count == 2:
            return  # return 뒤에 값이 없으면 그 즉시 빠져나간다.
        
        
        print(message)
        
def my_divmod(num1:int, num2:int):
    mok = num1 // num2  # 몫
    nam = num1 % num2   # 나머지
    return mok, nam

mok, nam = my_divmod(10, 3)
print(mok, nam)

values = my_divmod(10, 3)
print(values[0], values[1])



# 다중 반환 함수(내장 함수)
mok, nam = divmod(10, 3)    # python은 다중 반환이 가능하다.
print(mok, nam)

values = divmod(10, 3)  # tuple로 반환한다.
print(values) # 리스트 형식으로도 호출이 가능하다.



        
# greet('안녕하세요.', count=5)
# greet('반갑습니다.')
    
# show(1,2,3,4,5, horiz=1)
# show(1,2,3,)