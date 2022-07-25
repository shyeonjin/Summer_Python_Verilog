# 상속 관계와 포함 관계 알아보기
# 상속 관계
class Person:
    def greeting(self):
        print("안녕하세요")

class Student(Person):
    def study(self):
        print("공부하기")
    
# 포함관계
class Person1:
    def greeting(self):
        print('안녕하세요.')
 
class Person1List:
    def __init__(self):
        self.person1_list = []   
 
    def append_person(self, person):    
        self.person1_list.append(person)

a=Person1List()
a.append_person(1)
print(a.person1_list)