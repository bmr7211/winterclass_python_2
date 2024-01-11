'''
number = int(input('정수 입력: '))

sum = 1
for i in range(1, number+1):
    sum *= i

print('{0}!은 {1}이다.'.format(number, sum))
'''

for i in range(3):
    for j in range(2):
        print('i : {0}, j : {1}'.format(i, j))
    print('-----')
