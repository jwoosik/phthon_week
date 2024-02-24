'''
현재 10,000원을 가지고 있습니다. 얼마를 사용할 것인지 반복해서 입력받아
10,000원을 모두 사용하세요.
0 이하의 금액은 사용할 수 없으며, 현재 가지고 있는 돈보다 더 큰 금액도 사용할 수 없습니다.

현재 10000원이 있습니다.
사용할 금액 입력 >>> 5000
현재 5000원이 있습니다.

사용할 금액 입력 >>> -5000
0 이하의 금액은 사용할 수 없습니다.

사용할 금액 입력 >>> 6000
1000원이 부족합니다.

사용할 금액 입력 >>> 4000
현재 1000원이 있습니다.

사용할 금액 입력 >>> 1000
현재 0원이 있습니다.
'''


# total = 10000

# while True:
#     print(f'현재 {total}원이 있습니다.')
#     money = int(input('사용할 금액 입력 >>> '))
    
#     if money <= total:
#         total -= money
        
#     if money <= 0:
#         print('0 이하의 금액은 사용할 수 없습니다.')
    
#     if money > total:
#         print(f'{money-total}원이 부족합니다.')
        

# print('현재 0원이 있습니다.')
        
total = 10000

while total > 0:
    print(f'현재 {total}원이 있습니다.')
    money = int(input('사용할 금액 입력 >>> '))
    
    if total == 0:
        break
        
    elif money <= 0:
        print('0 이하의 금액은 사용할 수 없습니다.')
    
    elif money > total:
        print(f'{money - total}원이 부족합니다.')
    
    else:
        total -= money

print(f'현재 {total}원이 있습니다.')
        
