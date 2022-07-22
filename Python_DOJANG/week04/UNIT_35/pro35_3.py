# 클래스 메서드 사용하기
class Person:
    count = 0 
 
    def __init__(self):
        Person.count += 1  

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count)) 
 
j=Person()
ma=Person()
 
Person.print_count()