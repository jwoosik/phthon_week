'''
키(key)가 '과목명', 값(value)이 '점수'인 marks 딕셔너리를 전달하면
해당 딕셔너리에 저장된 점수들의 평균을 반환하는 get_average() 함수룰 구현하세요.

함수 정의)
반환값: 평균
함수 이름: get_average()
매개변수: mark (딕셔너리)

호출예)
marks = {'국어':90, '영어':80, '수학':85}
average = get_average(marks)
print('평균은 {}점입니다.'.format(average))

출력형식)
평균은 85.0점입니다.
'''

def get_average(marks:dict) -> float:
    # total = marks['국어'] + marks['영어'] + marks['수학']
    total = 0
    for key in marks:
        total += marks[key]
        
    return total / len(marks)
    
marks = {'국어':90, '영어':80, '수학':85}   # 좌: value / 우: key
avg = get_average(marks)

print(f'평균은 {avg:.1f}점입니다.')

# marks = {'국어':90, '영어':80, '수학':85}
# average = (marks[0] + marks[1] + marks[2]) / len(marks)
# print(f'평균은 {average}점입니다.'.format(average))