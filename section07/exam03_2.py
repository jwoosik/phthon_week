'''
사용자로부터 임의의 양의 정수를 하나 입력받은 뒤
그 숫자만큼 과일 이름을 입력받아서 basket이라는
세트에 저장하는 프로그램을 만드세요
'''

# len(basket) ==> 개수를 반환
'''
basket = set()
number = int(input('몇 개의 과일을 보관할까요? >>> '))
while 
basket.add() # 데이터 추가
'''

basket = set()
number = int(input('몇 개의 과일을 보관할까요? >>> '))
while len(basket) < number: # basket 개수가 number보다 작을 때까지 반복
    fr = input(f'{len(basket)+1}번째 과일을 입력하세요 >>> ')
    basket.add( fr )
print(basket)

'''
basket = {'사과','사과','포도'}
print(len(basket))
'''