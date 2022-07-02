# 심사문제: 온라인 할인 쿠폰 시스템 만들기
# 가격과 쿠폰이름을 각 줄에 입력 할인된 가격 프린트

money=int(input("금액을 적으세요:"))
cash=input("쿠폰을 적으세요")
if cash=="Cash5000":
    money-=5000
# elif사용시 
#elif cash=="Cash3000":
#    money-=3000

if cash=="Cash3000":
    money-=3000     

print("할인된 가격: %d"%money)