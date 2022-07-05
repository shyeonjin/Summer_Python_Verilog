# 반복문으로 딕셔너리의 키-값 쌍을 모두 출력하기
x={'a':10, 'b':20,'c':30,'d':40}
for i in x:
    print(i,end="")
print()
for key,value in x.items():
    print(key,value)


for key,value in {'a':10, 'b':20,'c':30,'d':40}.items():
    print(key,value)

# 딕셔너리의 키만 출력하기
for key in x.keys():
    print(key,end="")
print()

# 딕셔너리의 값만 출력하기
for value in x.values():
    print(value,end="")
print()