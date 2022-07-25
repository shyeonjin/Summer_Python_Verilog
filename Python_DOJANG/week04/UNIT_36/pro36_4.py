# 메서드 오버라이딩 사용하기
class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')
 
james=Student()
james.greeting()


class Person1:
    def greeting(self):
        print('안녕하세요.')
 
class Student1(Person):
    def greeting(self):
        super().greeting()    
        print('저는 파이썬 코딩 도장 학생입니다.')
 
james =Student1()
james.greeting()