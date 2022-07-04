# for 반복문으로 1차원 리스트 만들기
a=[]
for i in range(10):
    a.append(0)

print(a)

# for 반복문으로 2차원 리스트 만들기
a=[]
for i in range(3):
    line=[]
    for j in range(2):
        line.append(0)
    a.append(line)
print(a)

# 리스트 표현식으로 2차원 리스트 만들기
a=[[0 for j in range(2)] for i in range(3)]
print(a)

# 톱니형 리스트 만들기
a=[3,1,3,2,5]
b=[]

for i in a:
    line=[]
    for j in range(i):
        line.append(0)
    b.append(line)
print(b)

a=[[0]*i for i in [3,1,3,2,5]]
print(a)

# sorted로 2차원 정렬
students=[
    ['john','C',19],
    ['maria',"A",25],
    ['andrew',"B",7]
]
print(sorted(students,key=lambda student: student[1]))
print(sorted(students,key=lambda student: student[2]))



# 2차원 리스트의 할당과 복사 알아보기

a=[[10,20],[30,40]]
b=a
b[0][0]=500
print(a,b)

a=[[10,20],[30,40]]
import copy
b=copy.deepcopy(a)
b[0][0]=500
print(a,b)