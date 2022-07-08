# 함수의 결과를 반환하기
def add(a,b):
    return a+b

x=add(1,2)
print(x)


# 매개변수는 없고 반환값만 있는 함수
def one():
    return 1

x=one()
print(x)

# retrun으로 함수 중간에서 빠져나오기
def not_ten(a):
    if a==10:
        return
    print(a,"입니다",sep='')


not_ten(5)
not_ten(10)
