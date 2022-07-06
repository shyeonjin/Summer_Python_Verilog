# 집합 연산 사용하기
a={1,2,3,4}
b={3,4,5,6}
# 합집합
print(a|b)
print(set.union(a,b))

# 교집합
print(a&b)
print(set.intersection(a,b))

# 차집합
print(a-b)
print(set.difference(a,b))

# 대칭 차집합
print(a^b)
print(set.symmetric_difference(a,b))

# 집합 연산 후 할당 연산자 사용하기
a={1,2,3,4}
a|={5}
print(a)
a={1,2,3,4}
a.update({5})
print(a)


a={1,2,3,4}
a&={0,1,2,3,4}
print(a)

a={1,2,3,4}
a.intersection_update({0,1,2,3,4})
print(a)


a={1,2,3,4}
a-={3}
print(a)


a={1,2,3,4}
a.difference_update({3})
print(a)

a={1,2,3,4}
a^={3,4,5,6}
print(a)

a={1,2,3,4}
a.symmetric_difference_update({3,4,5,6})
print(a)


# 부분 집합과 상위집합 확인하기

a={1,2,3,4}
print(a<={1,2,3,4})
print(a.issubset({1,2,3,4,5}))
print(a<{1,2,3,4,5})

print(a>={1,2,3,4})
print(a.issuperset({1,2,3,4}))

print(a>{1,2,3})

# 세트가 같은지 다른지 확인하기
a={1,2,3,4}
print(a=={1,2,3,4})
print(a=={4,1,2,3})

print(a!={1,2,3})

# 세트가 겹치지 않는지 확인하기
a={1,2,3,4}
print(a.isdisjoint({5,6,7,8}))
print(a.isdisjoint({3,4,5,6}))