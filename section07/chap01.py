'''
파이썬에서의 for 반복문
일반적으로 파이썬에서의 for문은 시퀀스와 같이 사용된다.
시퀀스: 문자열, 리스트, 튜플 ===> 인덱싱이 가능한 자료 구조
비시퀀스하고도 같이 사용되는 경우도 있다
비시퀀스: 세트, 딕셔너리
Range: 범위(순서가 있는 범위)
'''

li = [10, 20, 30, 50, 80, 100]
# li에 있는 모든 아이템들을 num이라는 변수에 대입하면서 반복 수행한다.
for num in li:
    print(num) # li 변수에 num 변수로 넣고 li에 있는 문자를 순서대로 출력
    
s = 'Hello Python'
for ch in s:
    print(ch)
    
# li를 튜플로 바꾼다
tp = tuple(li)
for num in tp:
    print(num)
    
li = ['파이썬', '자바', 'C/C++', '코틀린']
for s in li:
    print(s)


print(range(5))
li = list(range(5)) # range(n) 0 ~ n-1까지 데이터가 생성된다.
print( li )

# list 대신 range으로도 사용 가능
li = list(range(5,10)) # range(start, end) s ~ e-1까지 데이터가 생성된다.
print( li ) # 5, 6, 7, 8, 9

li = list(range(1,10,2)) # range(start, end, step) start ~ end-1까지 step씩 건너뛰면서 데이터를 생성
print( li ) # 1, 3, 5, 7, 9

for num in range(5):    # 0, 1, 2, 3, 4 몇번 반복할지 카운트
    print(num, end='\t')

print()

for num in range(1,6): # 1 ~ 6-1까지 반복
    print(num, end='\t')
    
print()

for num in range(5):    # 반복 횟수를 지정해야 될때도 range()를 사용한다.
    print('Hello Python')
    
    
dan = int(input('구구단을 출력할 단수를 입력하세요 >>>'))
for num in range(1, 10):
    print(f'{dan}x{num}={dan*num}')