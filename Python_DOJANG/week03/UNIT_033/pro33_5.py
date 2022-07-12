# 연습문제: 호출 횟수를 세는 함수 만들기
from re import U


def counter():
    i=0
    def count():
        nonlocal i
        i+=1
        return i
    return count


c=counter()
for i in range(10):
    print(c(),end=" ")