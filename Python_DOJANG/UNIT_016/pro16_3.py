# 시퀀스 객체로 반복하기
# 리스트 반복
a=[10,20,30,40,50]
for i in a:
    print(i)

# 튜플 반복 
fruits=('apple','orage','grape')
for fruit in fruits:
    print(fruit)


# 문자열 반복
for letter in "Python":
    print(letter,end=" ")
print()

# 뒤집어서 출력 (reversed 활용)
for letter in reversed("Python"):
    print(letter,end=" ")