# break로 반복문 끝내기
# while에서 break로 반복문 끝내기
i=0
while True:
    print(i)
    i+=1
    if i ==100:
         break

# for에서 break로 반복문 끝내기
for i in range(10000):
    print(i)
    if i==100:
        break