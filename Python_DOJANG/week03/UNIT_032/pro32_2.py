# 람다 표현식과 map, filter, reduce 함수 활용하기

# 람다 표현식에 조건부 표현식 사용하기

a=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x :str(x) if x % 3==0 else x, a)))


# 람다 표현식에서 if를 사용하면 else를 무조건 사용해야한다.
print(list(map(lambda x: str(x) if x==1 else float(x)if x==2 else x+10,a)))


# map애 객체를 여러 개 넣기
a=[1,2,3,4,5]
b=[2,4,6,8,10]
print(list(map(lambda x,y:x*y,a,b)))


# filter 사용하기
def f(x):
    return x>5 and x<10
a=[8,3,2,10,15,7,1,9,0,11]
print(list(filter(f,a)))

# reduce 사용하기

def f(x,y):
    return x+y
a=[1,2,3,4,5]
from functools import reduce
print(reduce(f,a))


print(reduce(lambda x,y:x+y,a))


# map, filter, reduce
a=[8,3,2,10,15,7,1,9,0,11]
print([i for i in a if i>5 and i<10])

a=[1,2,3,4,5]
x=a[0]
for i in range(len(a)-1):
    x=x+a[i+1]

print(x)