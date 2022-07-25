# 기반 클래스의 속성 사용하기
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장'
 
james = Student()
print(james.school)
# print(james.hello)   


# super()로 기반 클래스 초기화하기
class Person2:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student1(Person2):
    def __init__(self):
        print('Student __init__')
        super().__init__()              
        self.school = '파이썬 코딩 도장'
 
james = Student1()
print(james.school)
print(james.hello)

# 기반 클래스를 초기화하기 않아도 되는 경우
class Person5:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student5(Person5):
    pass
 
james = Student5()
print(james.hello)