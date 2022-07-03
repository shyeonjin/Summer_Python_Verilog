# 심사문제: 리스트의 마지막 부분 삭제하기
# 리스트의 마지막요소 5개 삭제 후 튜플로 출력
p=input().split()
l=list(p)
del l[-5:]
print(tuple(l))
