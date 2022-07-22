# 비공개 속성 사용하기
class Person:
    def __init__(self,name,age,address):
        self.hello="안녕하세요"
        self.name = name
        self.age=age
        self.address=address

maria=Person('마리아',20,'서울')
print(maria.name)
print(maria.address)




class Person1:
    def __init__(self,name,age,address,wallet):
        self.name=name
        self.age=age
        self.address=address
        self.__wallet=wallet

maria1=Person1('마리아',20,'서울',111)
# maria1.__wallet -=11111

class Person2:
    def __init__(self,name,age,address,wallet):
        self.name=name
        self.age=age
        self.address=address
        self.__wallet=wallet

    def pay(self,amount):
        self.__wallet -=amount
        print('이제{0}원 남았습니다.'.format(self.__wallet))


mama=Person2('마리아',20,'서울',111)
mama.pay(1000)


# 비공개 메서드 사용하기
class Person4:
    def __init__(self):
        print("Hello")
    
    def hello(self):
        self.__greeting()
j=Person4()
j.__greeting() # 불가능 