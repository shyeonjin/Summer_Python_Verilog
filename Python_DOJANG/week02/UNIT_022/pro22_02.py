#리스트의 할당과 복사 알아보기
a=[0,0,0,0]
b=a
print(a is b)
# 변수 이름만 다를 뿐 리스트 a와 b는 같은 객체
# b의 요소를 변경하면 a,b와 모두 반영
b[2]=99
print(a,b)

# a,b를 두개로 만들려면 copy 매서드 사용
a=[0,0,0,0,0]
b=a.copy()
print(a is b)
print(a == b)
b[2]=99
print(a,b)