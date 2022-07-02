# 심화문제: 교통카드 시스템 만들기
# 교통카드 차감이벤트 
# 나이 입력후 나이에 따른 교통요금 할인 
age=int(input("나이 입력"))
money=9000
if 7<=age<=12:
    money-=650
  
elif 13<age<=18:
    money-=1050
 
elif age>19:
    money-=1250

print(money)
   