# 반복문으로 세트의 요소를 모두 출력하기

a={1,2,3,4}
for i in a:
    print(i)

for i in {1,2,3,4}:
    print(i)


# 세트 표현식 사용하기
a={i for i in 'apple'}
print(a)


# 세트 표현식에 if 조건문 사용하기
a={i for i in 'pineapple' if i not in 'apl'}
print(a)