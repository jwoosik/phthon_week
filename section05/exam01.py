# 1. 시험 점수를 입력받아서 ...
# 100~90: A
# 80~89: B
# 70~79: C
# 60~69: D
# 0~59: F

result = int(input('점수를 입력하세요 >>> '))
grade = 'F'
if result >= 90:
    grade = 'A'
elif result >= 80:
    grade = 'B'
elif result >= 70:
    grade = 'C'
elif result >= 60:
    grade = 'D'

print(f'점수는 {result}점이고, 학점은 {grade}학점입니다.')

