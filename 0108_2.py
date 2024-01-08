'''
score = int(input('점수 입력: '))

if score >= 60:
    print('Pass')
else:
    print('Nonpass')

###삼항 연산자

result = 'pass'  if score >= 60 else 'nonpass'
print(result)
'''

gender = input('gender : ')

result = 'W' if gender == '여자' else 'M'
print(result)
