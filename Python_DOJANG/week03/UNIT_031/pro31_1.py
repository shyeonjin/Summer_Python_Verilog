# 함수에서 재귀호출 사용하기


# 재귀호출 사용하기
def hello():
    print("Hello,world!")
    hello()
# hello()

# 재귀호출에 종료 조건 만들기
def hello1(count):
    if  count==0:
        return
    print("Hello,world!",count)
    count-=1
    hello1(count)

    
hello1(5)
