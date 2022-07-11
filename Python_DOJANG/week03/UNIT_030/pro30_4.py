# 매개변수에 초깃값 지정하기
def personal_info(name,age,address="비공개"):
    print("이름: ",name)
    print("나이: ",age)
    print("주소: ",address)

personal_info("홍길동",30)
personal_info("홍길동",30,'서울')


# 초기값이 지정된 매개변수의 위치
# def personal_info(name,addres="비공개",age):
#     print("이름: ",name)
#     print("나이: ",age)
#     print("주소: ",address)


# 초기값이 지정된 매개변수는 뒤쪽으로
def personal_info1(name, age, address='비공개'):
    pass
def personal_info2(name, age=0, address='비공개'):
    pass
def personal_info3(name="비공개", age=0, address='비공개'):
    pass