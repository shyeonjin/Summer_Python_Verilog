# 심사문제: 산 모양으로 별 출력하기
# 삼각형의 높이가 입력된다. 
high=int(input("높이를 적으세요: "))

for i in range(high):
    for j in range(high*2-1):
        if   j<(high-i-1):
            print(" ",end="")
        elif j>(high-1+i):
            print(" ",end="")
        else:
                print("*",end="")
    print()







