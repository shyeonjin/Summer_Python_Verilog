# 리스트 요소 추가하기
# append: 요소 하나를 추가, extend: 리스트를 연결하여 확장,insert: 특정 인덱스에 요소 추가

# 리스트에 요소 하나 추가하기
a=[10,20,30]
a.append(500)
print(a)
print(len(a))
a=[]
a.append(10)
print(a)

# 리스트 안에 리스트 추가하기
a=[10,20,30]
a.append([500,600])
print(a)
print(len(a))

# 리스트 확장하기
a=[10,20,30]
a.extend([500,600])
print(a)
print(len(a))


# 리스트의 특정 인덱스에 요소 추가하기
a=[10,20,30]
a.insert(2,500)
print(a)
print(len(a))

# 리스트 맨 처음에 추가
a=[10,20,30]
a.insert(0,500)
print(a)
print(len(a))

# 리스트 마지막에 추가
a=[10,20,30]
a.insert(len(a),500)
print(a)
print(len(a))

# 리스트에 리스트 삽입
a=[10,20,30]
a.insert(1,[500,600])
print(a)

# 슬라이싱 이용해서 추가
a=[10,20,30]
a[1:1]=[500,600]
print(a)

# 리스트에서 요소 삭제하기
# pop: 마지막 요소 또는 특정 인덱스의 요소를 삭제
# remove: 특정 값을 찾아서 삭제

# 리스트에서 특정 인덱스의 요소를 삭제하기
a=[10,20,30]
a.pop()
print(a)

a=[10,20,30]
a.pop(1)

print(a)

# del 사용가능
a=[10,20,30]
del a[1]
print(a)

# 리스트에서 특정 값을 찾아서 삭제하기
a=[10,20,30]
a.remove(20)
print(a)

# 리스트에 같은 값이 여러개 있을 경우 처음 찾은 값을 삭제
a=[10,20,30,20]
a.remove(20)
print(a)

# 리스트에서 특정 값의 인덱스 구하기
a=[10,20,30,15,20,40]
print(a.index(20))


# 특정 값의 개수 구하기
a=[10,20,30,15,20,40]
print(a.count(20))

# 리스트의 순서를 뒤집기
a=[10,20,30,15,20,40]
a.reverse()
print(a)

# 리스트의 요소를 정렬
a=[10,20,30,15,20,40]
a.sort()
print(a)

b=[10,20,30,15,20,40]
print(sorted(b))

# 리스트의 모든 요소 삭제하기
a=[10,20,30]
a.clear()
print(a)

# 리스트를 슬라이스로 조작하기
a=[10,20,30]
a[len(a):]=[500]
print(a)

a=[10,20,30]
a[len(a):]=[500,600]
print(a)