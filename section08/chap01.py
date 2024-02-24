'''
반복문에서 break문과 continue 문

break: 반복문을 그 즉시 탈출한다, 해당 반복문만 탈출한다.
continue: 반복문의 Head 부분으로 처리를 이동시킨다.
'''
# while문은 반복 횟수가 명확하지 않은 경우가 많다.  
# i = 1
# while True:
#     if i>100: break # i가 100을 초과하면 탈출
#     while True:
#         print('python')
#         if i >= 10: break   # break 문은 현재 break가 소속되어 있는 while문을 탈출한다.
#         i += 1
'''
while True: # 조건식을 넣을 수 있음. 무한 반복
    print('python')
''' 

# for문은 반복 횟수가 명확한 경우가 많다.
# for n in range(100):
#     if n >= 50: break # 특정 조건이 되었을 때 현재 소속되어 있는 반복문을 탈출한다.
#     print(n)


print('for문 진입')
for n in range(10):
    if n % 2 == 1: continue
    print(n)

print('for문 끝남')

print('while문 진입')
n = 0
while n < 10:
    if n % 2 == 1: 
        n += 1      # 이 부분이 없으면 무한 반복된다.
        continue
    print(n)
    n += 1
    
print('while문 끝남')