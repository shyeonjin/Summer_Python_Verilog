# 클로저 사용하기

# 변수의 사용 범위 알아보기
x=10
def foo():
    print(x)
foo()
print(x)
def foo1():
    x=10
    print(x)
foo1()
# 불가능 print(x)

# 함수 안에서 전역 변수 변경하기
x=10
def foo2():
    x=20
    print(x)

foo2()
print(x)

x=10
def foo3():
    global x
    x=20
    print(x)

foo3()
print(x)


x= None
def foo4():
    global x
    x=20
    print(x)

foo4()
print(x)

# 네임스페이스
x=10
print(locals())

def foo5():
    x=10
    print(locals())
foo5()