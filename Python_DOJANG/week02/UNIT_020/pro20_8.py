# 심사문제:5와 7의 배수, 공배수 처리하기
# 표준입력으로 두 개의 정수를 입력(첫 번째 범위 1~1000,두 번째 범위 10~1000)
# 첫 번째는 항상 두 번째보다 작다.
# 첫 번째부터 두 번째까지 숫자를 출력하면서 5의 배수일 때는 "Fizz",
# 7의 배수일 때는 "BUzz" 5와 7의 공배수일 때는 "FizzBuzz"출력

first,second=map(int,input("두 정수를 입력하세요: ").split())

for i in range(first,second+1):
    print("Fizz"*(i%5==0)+"Buzz"*(i%7==0) or i)