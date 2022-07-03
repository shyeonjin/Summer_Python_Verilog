# elif 사용하기
# if 조건문:
#    코드1
# elif 조건문:
#    코드2
from tkinter import Button


x=20
if x==10:
    print("10입니다")
elif x==20:
    print("20입니다")

# if,elif,else 모두 사용
x=30

if x==10:
    print("10입니다")
elif x==20:
    print("20입니다")
else:
    print("10도 20도 아닙니다.")


# 음료수 자판기 만들기
butten= int(input())

if butten==1:
    print('콜라')
elif butten==2:
    print("사이다")
elif butten==3:
    print("환타")
else:
    print("제공하지 않는 메뉴")