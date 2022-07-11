#  위치 인수와 리스트 언패킹 사용하기
print(10,20,30)
def print_numbers(a,b,c):
    print(a)
    print(b)
    print(c)
print_numbers(1,2,3)



# 언패킹 사용하기
x=[10,20,30]
print(*x)


# 가변 인수 함수 만들기
def print_numbers(*args):
    for arg in args:
        print(arg)

print_numbers(10)
print_numbers(10,20,30,40)


x=[10]
y=[10,20,30,40]
print(print_numbers(*x))
print(print_numbers(*y))
