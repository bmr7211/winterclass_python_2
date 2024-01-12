'''
i = 0
while i < 3:
    print('while_hi')
    i += 1

for i in range(3):
    print('for_hi')


i = 0
summ = 0

while i < 11:
    summ += i
    i += 1
print(summ)


i = 0
result = 0

while i <= 10:
    if i % 2 == 0:
        result += i
    i += 1
print(result)
'''

n = int(input('구구단: '))

i = 1
mul = 1
while i <= 9:
    mul = n * i
    print('{0} * {1} = {2}'.format(n, i, mul))
    i += 1
