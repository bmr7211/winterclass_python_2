'''
students = int(input('학생 수: '))

i = 0
summ = 0
while i < students:
    score = float(input('성적: '))
    summ += score
    i += 1

average = summ / students
print('score: %.1f, average: %.1f' % (score, average))


summ = 0
a, b = 0, 0

while True:
    a = int(input('first: '))
    if a == 0:
        break
    b = int(input('second: '))

    summ = a + b
    print('{0} + {1} = {2}'.format(a, b, summ))

print('input zero --> break')
'''

summ, i = 0, 0

for i in range(1, 101):
    if i % 3 == 0:
        continue
    summ += i

print('3의 배수를 제외한 1부터 100까지의 합:', summ)
