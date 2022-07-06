# 심사문제: 공약수 구하기
# 표준 입력으로 양의 정수 두 개가 입력
# 두 숫자의 공약수를 세트형식으로 구하고 출력은 공약수의 합으로

first,second=map(int,input("정수를 입력하세요: ").split())
firstset=set()
secondset=set()
for i in range(1,first+1):
    if first%i==0:
        firstset.add(i)

for i in range(1,second+1):
    if second%i==0:
        secondset.add(i)

finset=firstset&secondset

print(sum(finset))