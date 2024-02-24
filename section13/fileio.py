'''
파일 입출력

파일 종류: 텍스트 파일(Text File), 바이너리 파일(Binary File) => 특정 뷰어가 필요함

파일 입력: 파일로부터 데이터를 읽는 것 (Read File, Load)
파일 출력: 데이터를 파일에 저장하는 것 (Write File, Save)

규칙)
파일을 연다(읽기 또는 쓰기 모드 중 한가지 방법으로만 열 수 있다.)
파일에 쓴다(또는 파일로부터 읽는다.)
파일을 닫는다

File Mode => 모드 중 하나씩 쓸 수 있음
ex) rt, wt
r: 읽기 모드 (read)
w: 쓰기 모드 (write)
a: 추가 모드 (append)

t: 텍스트 모드 (text)
b: 바이너리 모드 (binary)

'''

# path: file 위치 + 파일명

# 파일 출력
# 파일을 연다
file = open('path', 'wt')
# 파일을 쓴다.
file.write('data')
file.write('data')
file.write('data')
file.write('data')
file.write('data')
# 파일을 닫는다
file.close()

# 파일 입력
# 파일을 연다
file = open('path', 'r')
# 파일을 읽는다
file.read('data')
# 파일을 닫는다
file.close()

with open('path', 'r') as file:
    file.read()    
# with문을 빠져나오면 file.close()를 자동으로 해준다.





