# while 반복문
# 초기값을 1부터 시작
i=1
while i<=100:
    print("Hello,world!",i)
    i+=1

# 초기값을 감소시키기
i=100
while i>0:
    print("Hello,world!",i)
    i-=1

# 입력한 횟수대로 반복하기
count=int(input("반복할 횟수를 입력하시오: "))

i=0
while i<count:
    print("Hello,world!",i)
    i+=1

count=int(input("반복할 횟수를 입력하시오: "))


while count>0:
    print("Hello,world!",count)
    count-=1