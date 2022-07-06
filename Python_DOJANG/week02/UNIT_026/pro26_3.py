# 세트 조작하기

# 세트에 요소를 추가하기
a={1,2,3,4}
a.add(5)
print(a)

# 세트에서 특정 요소를 삭제하기

a.remove(3)
print(a)

a.discard(2)
print(a)
a.discard(3)
print(a)

# 세트에서 임의의 요소를 삭제하기
a={1,2,3,4}
print(a.pop())
print(a)

# 세트의 모든 요소를 삭제하기
a.clear()
print(a)


# 세트의 요소 개수 구하기
a={1,2,3,4}
print(len(a))