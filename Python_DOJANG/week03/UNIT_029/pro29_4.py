# 함수에서 값을 여러 개 반환하기

def add_sub(a,b):
    return a+b,a-b

x,y=add_sub(10,20)
print(x,y)
x=add_sub(10,20)
print(x)
print(type(x))


# 값 여러 개를 직접 반환하기
def one_two1():
    return (1,2)
print(one_two1())
def one_two2():
    return [1,2]


print(one_two2())