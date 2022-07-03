# 반복 횟수가 정해지지 않은 경우
# random사용
import random

print(random.random())

# 랜덤의 범위를 지정하는 함수 randint
print(random.randint(1,6))

# 주사위 3이 나올 때까지 돌아가는 Code
i=0
while i!=3:
    i=random.randint(1,6)
    print(i)
print()
# random.chioce 시퀀스 객체에서 무작위로 뽑음
dice=[1,2,3,4,5,6]
print(random.choice(dice))
