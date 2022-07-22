# 속성 사용하기
class Person:
    def __init__(self):
        self.hello="안녕하세요"
    def greeting(self):
        print(self.hello)

j=Person()
j.greeting()

# 인스턴스를 만들 때 값 받기

class Person1:
    def __init__(self,name,age,address):
        self.hello="안녕하세요"
        self.name=name
        self.age=age
        self.address=address

    def greeting(self):
        print('{0} 저는 {1}입니다'.format(self.hello,self.name))

maria=Person1("마리아",20,"서울")
maria.greeting()



# 클래스의 위치 인수, 키워드 인수
class Person2:
    def __init__(self,*args):
        self.hello="안녕하세요"
        self.name=args[0]
        self.age=args[1]
        self.address=args[2]
m=Person2(*["마리아",20,"서울"])



class Person3:
    def __init__(self,**kwargs):
        self.name=kwargs['name']
        self.age=kwargs['age']
        self.address=kwargs['address']

ma1=Person3(name='마리아', age=20, address='서울시 서초구 반포동')
ma2 = Person3(**{'name': '마리아','age': 20, 'address':'서울시 서초구 반포동'})