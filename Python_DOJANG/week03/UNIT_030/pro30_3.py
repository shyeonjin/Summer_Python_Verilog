# 키워드 인수와 딕셔너리 언패킹 사용하기

def personal_info(name,age,address):
    print("이름:",name)
    print("나이:",age)
    print("주소",address)


x={"name":"홍길동","age":30,"address":"서울시 용산구 이촌동"}
personal_info(**x)
personal_info(*{"name":"홍길동","age":30,"address":"서울시 용산구 이촌동"})


# **를 두 번 사용하는 이유

# *를 한 번 사용하면 key의 값
personal_info(*x)

personal_info(**x)

# 키워드 인수를 사용하는 가변 인수 함수 만들기
def personal_info1(**kwargs):
    for kw,arg in kwargs.items():
        print(kw,":",arg,sep="")


personal_info1(name="홍길동")
personal_info1(name="홍길동",age=30,address="서울 이촌동 ")


# 고정 인수와 가변 인수를 함께 사용하기
def personal_info2(name,**kwargs):
    print(name)
    print(kwargs)

personal_info2('홍길동')
personal_info2("홍길동",age=30,address="서울시 용산구")
personal_info2(**{"name":"홍길동","age":30,"address":"서울시 용산구 이촌동"})

# 위치 인수와 키워드 인수를 함께 사용하기
def custom_print(*args,**kwargs):
    print(*args,**kwargs)


custom_print(1,2,3,sep=":",end="")