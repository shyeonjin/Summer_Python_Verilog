# 심사문제: 재귀호출로 피보나치 수 구하기
# 입력으로 정수 한개 입력(10~30)

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)



num=int(input("정수를 입력하세요"))
print(fib(num))