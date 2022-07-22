# 클래스와 메서드 만들기
# class 클래스이름:
#   def 메서드(self)
#       코드




class Person:
    def greeting(self):
        print("Hello")

james=Person()
# 메서드 호출하기
james.greeting()

# 파이썬에서 흔히 볼 수 있는 클래스
a=int(10)
print(a)
b=list(range(10))
print(b)
c=dict(x=10,y=20)
print(c)

b.append(20)
print(b)

print(type(a))
print(type(b))
print(type(c))


# 빈 클래스 만들기
class Person1:
    pass

# 메서드 안에서 메서드 호출하기

class Person2:
    def greeting(self):
        print("hello")
    
    def hello(self):
        self.greeting()

j=Person2()
j.hello()

# 특정 클래스의 인스턴스인지 확인하기
print(isinstance(j,Person2))

def factorial(n):
    if not isinstance(n,int) or n<0:
        return None
    if n==1:
        return 1
    return n*factorial(n-1)


print(factorial(5))