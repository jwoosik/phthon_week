'''
모듈: 파이썬 파일
'''

import myutil as mu     # as는 파일 이름을 별칭으로 지정

total = mu.get_total(80, 90, 100)
avg = mu.get_average(total, 3)

# myutil 모듈로부터 get_total 함수만 가져온다. (원하는 함수만 가져옴)
from myutil import get_total as gt, get_average as ga   # as는 함수를 별칭으로 지정

total = gt(90, 100, 100)
avg = ga(total, 3)



