'''
조건문(if statement)
'''
num1 = 10
num2 = 5
if num1==10 and num2==5: # 파이썬 if문에선 :(콜론)으로 끝내야함 / 결과는 단 하나
    # 코드 블록이 만들어 지면서 
    # 위 조건문이 참일 때 분기된다
    print(num1) # 서브 블록
    print(num2) # 서브 블록
    
print('조건문 처리가 끝났습니다.') # 참/거짓 관계 없이 출력

if num1==10:
    print(f'{num1}의 값은 10입니다.')
else: # 여기서도 :(콜론) 필수
    print(f'{num1}의 값은 10이 아닙니다.')
    
isOk = True
li = [] # 빈 리스트 ==> False
nothing = "" # 빈 문자열 ==> False
num1 = 0 # 0이면 False, 0이 아닐 경우는 True

if isOk:
    print(isOk)
    
if li:      # if문의 조건으로 사용될 수 있고, 빈 리스트의 논리값은 False
    print(li)
    
if nothing: # 빈 문자열의 논리값은 False
    print(nothing)
    
if num1:    # 정수 0의 논리값은 False
    print(num1)
    
num1 = 10
if num1==0:
    print('num1은 0입니다.')
elif num1==1:
    print('num1은 1입니다.')
elif num1==2:
    print('num1은 2입니다.')
elif num1==3:
    print('num1은 3입니다.')
elif num1==4:
    print('num1은 4입니다.')
elif num1==5:
    print('num1은 5입니다.')
else:
    print('num1의 값을 알 수 없습니다.')
    
    
if num1==10:
    if num2==5: # 논리연산자 and와 동일한 조건
        print(num1)
        print(num2)
    else:
        print('num1은 10이고, num2는 5가 아닙니다.')
else:
    print('num1은 10이 아닙니다.') # num1의 값부터 False면 해당 값을 출력