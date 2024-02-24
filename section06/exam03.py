j = 1
while j <= 9: # 곱수
    i = 2
    while i <= 9: # i가 1증가할 때 j는 1~9까지 증가 / 단수
        print(f'{i}x{j}={i*j}', end='\t')
        i += 1
        
    j += 1
    print()