'''
영화 평점을 1부터 5사이의 정수로 입력받아서 해당 평점만큼 ★을 표시
표시할 수 있는 평점의 범위를 벗어나면 재입력을 요구하세요
'''



while True:
    star = '★'
    movie = int(input('이번 영화의 평점을 입력하세요 >>> '))
    if 1 <= movie <= 5:
        break
    else:
        print('평점은 1~5 사이만 입력할 수 있습니다.')

print(f'평점: {movie*star}')