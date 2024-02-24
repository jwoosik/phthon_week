'''
02-543-2109
02-2345-6789
032-789-0123
031-4567-8900

어떠한 형식의 전화번호 형태라도 국번만 추출하여 출력

전화번호를 입력하세요 >>> 02-543-2109
543
'''

tel_num = input('전화번호를 입력하세요 >>> ')
# start = tel_num.index('-') + 1
# end = tel_num.index('-', start)
# print(tel_num[start:end])

li = tel_num.split('-')
print(li[1])