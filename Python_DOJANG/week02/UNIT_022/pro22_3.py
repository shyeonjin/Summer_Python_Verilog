# 반복문으로 리스트의 요소를 모두 출력하기
# for 반복문으로 요소 출력하기
a=[38,21,53,62,19]
for i in a:
    print(i)

# 직접 지정해도 된다.
for i in [38,21,53,62,19]:
    print(i)

# 인덱스와 요소를 함께 출력하기
a=[38,21,53,62,19]
for index,value in enumerate(a):
    print(index,value)

# 인덱스를 1부터 출력하고 싶을 때

for index,value in enumerate(a):
    print(index+1,value)

# 파이썬스러운 방법
for index,value in enumerate(a,start=1):
    print(index,value)

# while 반복문으로 요소 출력하기
a=[38,21,53,62,19]
i=0
while i<len(a):
    print(a[i])
    i+=1

