# 심사문제:range로 튜플 만들기
# range의 시작 -10 끝 10 간격은 입력

p=int(input("간격을 입력하세요"))
t=tuple(range(-10,10,p))
print(t)