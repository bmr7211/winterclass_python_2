'''
for i in range(2, 10):
    for j in range(1, 10):
        mul = i * j
        print('{0} * {1} = {2}'.format(i, j, mul))
    print('-----')


for i in range(5):
    for j in range(10):
        print('*', end="")
    print('')
'''

line = int(input('line : '))

for i in range(line):
    for j in range(10):
        print('❤', end="")
    print('')
