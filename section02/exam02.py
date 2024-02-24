# s = input('프롬프트...')
# 사람
# person = {}
# name = {sora, woosic}
# age: 18
# role: 아빠, 엄마, 딸, 강아지, 고양이...

# {'name':'sora', 'age':18, 'role':'아빠'} 형식으로 출력

person = dict() # 생성자
person['name'] = input('이름을 입력하세요 >>>')
person['age'] = int(input('나이를 입력하세요 >>>'))
person['role'] = input('역할을 입력하세요 >>>')

person2 = dict() # 생성자
person2['name'] = input('이름을 입력하세요 >>>')
person2['age'] = int(input('나이를 입력하세요 >>>'))
person2['role'] = input('역할을 입력하세요 >>>')

person3 = dict() # 생성자
person3['name'] = input('이름을 입력하세요 >>>')
person3['age'] = int(input('나이를 입력하세요 >>>'))
person3['role'] = input('역할을 입력하세요 >>>')

li = []
li.append(person)
li.append(person2)
li.append(person3)

print(li)

neighbor = {}
# name: '땡땡마을'
# family: list

# 매크로(자동화), AI, 빅데이터, 웹(백엔드)