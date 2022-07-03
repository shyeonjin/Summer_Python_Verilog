# 입력한 횟수대로 반복하기
count=int(input("반복할 횟수를 입력하세요"))

i=0
while True:
    print(i)
    i+=1
    if i == count:
        break

# 입력한 숫자까지 홀수 출력하기
count=int(input("반복할 횟수를 입력하세요: "))

for i in range(count+1):
    if i %2==0:
        continue
    print(i)
