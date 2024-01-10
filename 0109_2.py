'''
number = int(input('숫자 입력: '))

sum = 0

for i in range(1, number+1):
    sum += i

print('1부터 {0}까지의 합 : {1}'.format(number, sum))
'''

quan = int(input('과목 수 : '))

sum = 0
average = 0

for i in range(0, quan):
    score = float(input('점수 : '))
    sum += score

average = sum / quan

print('과목 합 : {0}, 성적 평균 : {1}'.format(sum, average))
