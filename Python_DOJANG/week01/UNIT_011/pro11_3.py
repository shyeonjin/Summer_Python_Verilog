# 인데스 사용
a=[38,21,53,62,19]
print(a[0],a[1],a[2])
b=(38,21,53,62,19)
print(b[0],b[1])
r=range(0,10,2)
print(r[2])
hello="Hello, world!"
print(hello[7])

# 음수 인덱스 지정
a=[38,21,53,62,19]
print(a[-1],a[-5])
b=(38,21,53,62,19)
print(b[-1],b[-3])
r=range(0,10,2)
print(r[-3])
hello="Hello, world!"
print(hello[-4])

# 마지막 요소에 접근
a=[38,21,53,62,19]
print(a[len(a)-1])

# 요소에 값 할당
a=[0,0,0,0,0]
a[0]=38
a[1]=21
a[2]=53
a[3]=62
a[4]=19
print(a)
print(a[0],a[4])

# del로 요소 삭제
a=[38,21,53,62,19]
del a[2]
print(a)
