# 시작하는 숫자와 끝나는 숫자 
for i in range(5,12):
    print('Hello,world!',i)

# 증가폭 사용하기
for i in range(0,10,2):
    print("Hello,world",i)

# 숫자를 감소시키기
for i in range(10,0): # range는 기본 증가폭이 1이라 작동X
    print('Hello, world!',i)

for i in range(10,0,-1):
    print('Hello, world!',i)

# 입력한 횟수대로 반복하기

count = int(input("반복할 횟수를 입력하세요"))

for i in range(count):
    print("Hello, world!",i)