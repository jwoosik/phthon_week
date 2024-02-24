'''
while 반복문

while 논리식: // 참일 경우 다시 반복해서 실행, 논리식이 거짓이 될 때까지 반복 수행.
    명령문1
    명령문2
    명령문...
    
무한반복 중지 터미널에서 Ctrl + C
'''

i = 0
while i < 10:
    print(f'반복 {i}')
    i += 1
    
print(f'while 반복문이 종료되었습니다., i={i}')

until = int(input('반복 횟수를 입력하세요 >>> '))
i = 0 
while i < until:
    
    print(f'{i} / {until} 반복중...')
    i += 1
    
