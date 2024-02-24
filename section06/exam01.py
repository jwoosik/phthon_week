'''
1부터 100사이의 모든 정수 중에서 7의 배수만 출력하세요

7
14
21
''' 

i = 1
while i <= 100:
    # res = i & 7
    # if res==0:
    # if not res:
    if not (i % 7):print(i)
        
    i += 1
    