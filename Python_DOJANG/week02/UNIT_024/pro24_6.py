# 심사문제: 높은 가격순으로 출력하기
# 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력
# 각 가격은 ;으로 구분
# 높은 가격순으로 출력하고 가격의 길이는 9 천단위 콤마
price=input("가격을 입력하세요")
listpr=price.split(";")
listpr=[int(i) for i in listpr]
listpr=sorted(listpr,reverse=True)
for i in listpr:
    print("{0:>9,}".format(i))