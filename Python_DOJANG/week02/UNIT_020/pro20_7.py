# 연습문제 : 2와 11의 배수, 공배수 처리하기
# 2의 배수일 때 'Fizz' 11의 배수일 때 'Buzz'
# 2와 11의 공배수일 때 "FizzBuzz"출력
for i in range(1,101):
    if i%2==0 and i%11==0:
        print("FizzBuzz")
    
    elif i%2==0:
        print("Fizz")

    elif i%11==0:
        print("Buzz")

    else:
        print(i)