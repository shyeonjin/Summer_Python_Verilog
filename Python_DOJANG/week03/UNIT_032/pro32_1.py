# 람다 표현식 사용하기

# 람다 표현식으로 함수 만들기
def plus_ten(x):
    return x+10
print(plus_ten(10))
plus_1=lambda x:x+10
print(plus_1(1))

# 람다 표현식 자체를 호출하기
print((lambda x:x+10)(1))


# 람다 표현식 안에서는 변수를 만들 수 없다.
# 람다 표현식 안에서 새 변수선언은 안된다. 하지만 표현식 밖에 있는 변수는 사용가능
y=10
print((lambda x: x+y)(1))

# 람다 표현식을 인수로 사용하기
print(list(map(plus_ten,[1,2,3])))

print(list(map(lambda x: x+10,[1,2,3])))


# 람다 표현식으로 매개변수가 없는 함수 만들기

print((lambda :1)())
x=10
print((lambda :x)())
