# 함수 안에서 함수 만들기
from re import X


def print_hello():
    hello='Hello,world!'
    def print_message():
        print(hello)
    print_message()
print_hello()


# 지역 변수의 범위
def print_hello():
    hello='Hello,world!'
    def print_message():
        print(hello) # 바깥쪽 함수의 지역 변수를 사용


# 지역 변수 변경하기
def A():
    x=10        # A의 지역 변수 x
    def B():
        x=20    # x에 20 할당
    B()
    print(x)    # A의 지역 변수 x 출력
A()



def A1():
    x=10
    def B1():
        nonlocal x
        x=20

    B1()
    print(x)
A1()




# nonlocal이 변수를 찾는 순서
def A2():
    x=10
    y=100
    def B2():
        x=20
        def C():
            nonlocal x
            nonlocal y
            x=x+30
            y=y+300
            print(x)
            print(y)
        C()
    B2()
A2()


# global로 전역 변수 사용하기
x=1
def A3():
    x=10
    def B3():
        x=20
        def C3():
            global x
            x=x+30
            print(x)
        C3()
    B3()
A3()