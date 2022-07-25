# 클래스 상속
# 사람클래스를 학생 클래스로 만들기
class Person:
    def greeting(self):
        print("안녕하세요")

class Student(Person):
    def study(self):
        print("공부하기")


j=Student()
j.greeting()
j.study()



# 상속 관계 확인하기

print(issubclass(Student,Person))