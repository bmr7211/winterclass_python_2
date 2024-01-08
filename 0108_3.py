'''
fruits = ['딸기', '사과', '배']

fruits.append('귤')

if '딸기' in fruits:
    print('딸기 있음')
else:
    print('없음')
'''

import random

a = random.randrange(1, 7)
b = random.randrange(1, 7)

print('A의 주사위 숫자는 %d입니다.' % a)
print('B의 주사위 숫자는 %d입니다.' % b)

if a > b:
    print('A win')
elif a < b:
    print('B win')
else:
    print('A == B')
