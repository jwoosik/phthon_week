'''
결혼식에 참석하는 사람들의 축의금 명단을 만들고, 축의금 합계 구하기

함수정의)
반환값: 업음
함수이름: gift()
매개변수: 딕셔너리 dic, 사람 who, 축의금 money

wedding = {}
gift(wedding, '영희', 5)
gift(wedding, '철수', 3)
gift(wedding, '이모', 10)
print('축의금 명단: {}'.format(wedding))
print('전체 축의금: {}'.format(total))

'''


total = 0
def gift(wedding:dict, who:str, money:int) -> None:
    wedding[who] = money
    global total
    total += money

wedding = {}
gift(wedding, '영희', 5)
gift(wedding, '철수', 3)
gift(wedding, '이모', 10)

print(f'축의금 명단: {wedding}')
print(f'전체 축의금: {total}')