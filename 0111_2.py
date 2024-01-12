while True:
    a = int(input('첫 번째: '))
    b = int(input('두 번째: '))
    calc = input('연산자: ')

    if calc == '+':
        print('{0} + {1} = {2}'.format(a, b, a+b))
    elif calc == '-':
        print('{0} - {1} = {2}'.format(a, b, a-b))
    elif calc == '*':
        print('{0} * {1} = {2}'.format(a, b, a*b))
    elif calc == '/':
        print('{0} / {1} = {2}'.format(a, b, a/b))
    elif calc == '//':
        print('{0} // {1} = {2}'.format(a, b, a//b))
    elif calc == '%':
        print('{0} % {1} = {2}'.format(a, b, a%b))
    elif calc == '**':
        print('{0} ** {1} = {2}'.format(a, b, a**b))
    elif calc == 'e':
        print('The end')
        break
    else:
        print('wrong')
