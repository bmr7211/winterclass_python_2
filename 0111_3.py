'''
# 같은 눈이 나올 때까지 주사위 2개 던지기

import random

count = 0

while True:
    count += 1
    n1 = random.randrange(1, 7)
    n2 = random.randrange(1, 7)
    if n1 == n2:
        print('{0}. {1} == {2}'.format(count, n1, n2))
        break
    print('{0}. first: {1}, second: {2}'.format(count, n1, n2))
'''

# 1~5까지의 범위 안에서 나와 컴퓨터 간의 숫자 내기를 한다.
# 이기는 사람을 출력

import random
'''
while True:
    mychoice = int(input('1~5 숫자: '))
    print('mychoice =', mychoice, end=" ")
    comchoice = random.randrange(1, 6)
    print('comchoice =', comchoice)

    answer = random.randrange(1, 6)
    print('Answer =', answer)

    if mychoice == answer:
        print('Human Win')
        break
    elif comchoice == answer:
        print('Computer Win')
        break
    else:
        print('Replay')
'''
while True:
    mychoice = int(input('1~5 숫자: '))
    print('mychoice =', mychoice, end=" ")
    comchoice = random.randrange(1, 6)
    print('comchoice =', comchoice)

    if mychoice > comchoice:
        print('Human Win')
        break
    elif mychoice < comchoice:
        print('Computer Win')
        break
    else:
        print('Same')

