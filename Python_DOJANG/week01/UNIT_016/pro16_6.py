# 심사문제: 구구단 출력하기
#표준 입력으로 정수 입력 구구단 출력 문제
dan=int(input("단을 입력하세요: "))
for i in range(1,10):
    print("%d * %d = %d"%(dan,i, dan*i))