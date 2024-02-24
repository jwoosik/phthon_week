'''
700원짜리 음료수 자판기
돈을 넣으면 몇잔의 음료수를 뽑을 수 있는지, 잔돈은 얼마인지
모든 경우의 수를 출력

함수 정의
반환값: 없음
함수 이름: vending_machine()
매개변수: money (정수)

호출예)
vending_machine(3000)

출력형식)
음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
음료수 = 2개, 잔돈 = 1600원
음료수 = 3개, 잔돈 = 900원
음료수 = 4개, 잔돈 = 200원
'''

def vending_machine(money:int) -> None:
    value = 700
    count = 0
    while True:
        print(f'음료수 = {count}개, 잔돈 = {money}원')
        if money < value:
            break
        
        money -= value
        count += 1
        
vending_machine(3000)