# 세트 만들기
fruit={'strawberry','grape','orange','pineapple','cherry'}
print(fruit)
# 순서가 정해지지 않음 매 실행마다 값이 바뀜
# 중복될 수 없다.
fruit={'orange','orange','cherry'}

# 세트에 특정 값이 있는지 확인하기

fruit={'strawberry','grape','orange','pineapple','cherry'}
print('orange'in fruit)
print('peach'in fruit)
print('orange' not in fruit)
print('peach' not in fruit)

# set를 사용하여 세트 만들기
a=set('apple')
print(a)
b=set(range(5))
print(b)
c=set()
print(c)

# 세트안에 한글 넣기
a=set('안녕하세요')
print(a)

# 프로즌세트
a=frozenset(range(10))
print(a)