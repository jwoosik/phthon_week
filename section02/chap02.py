'''
Collection
list
tuple
set
dictionary
'''
li = [] # 빈 리스트를 생성한다.
li = [1,2,3,4,5]
print(li)
li.append(6) # 리스트에 6 값을 추가
li.append(7) # 리스트에 7 값을 추가
print(li) 
li.remove(1) # 리스트 내에서 1이라는 값을 삭제
print(li)

tp = tuple(li) # 튜플은 데이터의 묶음, 추가/수정/삭제 불가. 인덱싱 가능.
print(li[0])
print(tp[0])

s = set() # 인덱싱이 없음.
s.add(1)
s.add(2)
s.add(3)
s.add(1) # 중복 데이터는 허용하지 않음.
print(s)

# dictionary는 인덱싱 기능이 없음.
# Key : Value의 쌍(couple)으로 데이터를 관리한다.
di = dict() # 빈 딕셔너리를 생성.
di = {"tomato":"토마토", "banana":"바나나", "apple":"사과"} # 매우매우 중요 !
# 데이터를 관리. 위에서 아이템은 총 3개. 구별은 ,(쉼표). 
# 데이터는 항상 쌍으로 관리해야함. 앞 내용은 key, 뒤 내용은 value. 포커싱은 value에 두기.
# key 값을 알아야 데이터를 찾을 수 있음. 영한사전이라고 생각하면 이해가 쉬움.

# 파이썬에서 하는 방법
print(di)
di['orange'] = '오렌지' # ", ' 두개 다 사용 가능하지만 json 규격은 "을 사용하여야함. 파이썬은 무관.
# 딕셔너리명[key값] = value / 입력과 수정이 같은 방법. 없는 key값은 삽입, 있는 key값은 수정.
print(di) # orange라는 key값이 없으므로 삽입됨.
di["apple"] = "애플"
print(di) # apple이라는 key값이 있으므로 애플로 value 값이 수정됨.

print(di['tomato']) # tomato key값의 value 값을 출력.

some_fruit = di["banana"] # banana의 key값을 some_fruit 변수로 선언.
print(some_fruit) # some_fruit 변수를 출력.
some_fruit = di["tomato"]
print(some_fruit)
di.setdefault("tomato", "토마토")
di.update(tomato="토마토")

# pop은 데이터를 꺼내서 사용자한테 던져줌. 데이터를 무시하면 삭제하는 용도.
val = di.pop("tomato") # L value는 무조건 변수가 와야함 !
print(val)
print(di) # tomato는 삭제된 후 출력됨