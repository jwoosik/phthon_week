'''
임의의 정수를 입력받은 뒤 해당 값이 3의 배수인지 아닌지 판별하는 프로그램을 구현하세요.

정수를 입력하세요 >>> 14
14는 3의 배수가 아닙니다.

정수를 입력하세요 >>> 15
15는 3의 배수입니다.
'''

number = int(input('정수를 입력하세요 >>> '))
res = number % 3
# if res==0:
# if number % 3 == 0:
# if not res:

if res==0:
    print(f'{number}는 3의 배수입니다.')
else:
    print(f'{number}는 3의 배수가 아닙니다.')
    
