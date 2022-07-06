# 세트의 할당과 복사

a={1,2,3,4}
b=a
print(a is b)
b.add(5)
print(a,b)

a={1,2,3,4}
b=a.copy()
print(a is b)
print(a==b)

b.add(5)
print(a,b)