'''
for i in range(2, -1, -1):
    print('%d : 안녕하세요 for문 공부 중입니다.' % i, end=" ")


sum = 0

for i in range(1, 11):
    sum += i
    if i == 10:
        print(i, end="")
        break
    print(i, end="+")

print('=%d' % sum)


sum = 0

for i in range(1, 11):
    if i % 2 == 0:
        sum += i

print('합:', sum)
'''

lang = '안녕하세요 저는 신지윤입니다.'
for i in lang:
    print(i, end=" ")
