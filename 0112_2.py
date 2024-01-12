'''
# 이름을 입력받아서 리스트에 저장, 출력
family = int(input('가족 수: '))
namelist = []

i = 0
while i < family:
    name = input("name : ")
    namelist.append(name)
    i += 1

print(namelist)
'''

# 점수 4개를 입력받아서 최고 점수를 출력
'''
score = [56, 86, 36, 98]
print('최고 점수:', max(score))
'''
score = [0,0,0,0]

for i in range(4):
    score[i] = int(input('score: '))
print(score)

# 크기 비교
big = score[0]
for i in range(4):
    if score[i] > big:
        big = score[i]

print('biggest :', big)
