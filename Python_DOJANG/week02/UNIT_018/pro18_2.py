# continue로 코드 실행 건너뛰기
# for에서 continue로 코드 실행 건너뛰기
for i in range(100):
    if i % 2==0:
        continue
    print(i)

# while 반복문에서 continue로 코드 실행 건너뛰기
i=0
while i<100:
    i+=1
    if i%2==0:
        continue
    print(i)