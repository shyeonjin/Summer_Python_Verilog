# 리스트 표현식 사용하기
a=[i for i in range(10)]
print(a)

b=list(i for i in range(10))
print(b)

c=[i+5 for i in range(10)]
print(c)

d=[i*2 for i in range(10)]
print(d)

# 리스트 표현식에서 if 조건문 사용하기
a=[i for i in range(10) if i %2==0]
print(a)

b=[i+5 for i in range(10) if i%2==1]
print(b)

# for 반목문과 if 조건문을 여러 번 사용하기
a=[i*j for j in range(2,10) for i in range(1,10)]
print(a)