# 클래스 속성과 인스턴스 속성 알아보기
# 클래스 속성 사용하기
class Person:
    bag=[]
    
    def put_bag(self,stuff):
        self.bag.append(stuff)

j=Person()
j.put_bag('책')

maria=Person()
maria.put_bag("열쇠")

print(j.bag)
print(maria.bag)

print(Person.bag)

# 인스턴스 속성 사용하기
class Person1:
    def __init__(self):
        self.bag=[]
    
    def put_bag(self,stuff):
        self.bag.append(stuff)
j=Person1()
j.put_bag("책")

maria=Person1()
maria.put_bag("열쇠")

print(j.bag)
print(maria.bag)

# 비공개 클래스 속성 사용하기
class Knight:
    __item_limit =10

    def print_item_limit(self):
        print(Knight.__item_limit)

x=Knight()
x.print_item_limit()

# print(Knight.__item_limit)




# 독스트링 사용
class Person3:
    '''사람 클래스입니다.'''
    
    def greeting(self):
        '''인사 메서드입니다.'''
        print('Hello')

print(Person3.__doc__)             
print(Person3.greeting.__doc__)    
maria = Person3()
print(maria.greeting.__doc__)