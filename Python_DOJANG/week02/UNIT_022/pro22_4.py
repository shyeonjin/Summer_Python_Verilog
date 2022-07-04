# 리스트의 가장 작은 수, 가장 큰 수, 합계 구하기
# 가장 작은수와 가장 큰 수 구하기
a=[38,21,53,62,19]
smallest=a[0]
for i in a:
    if i<smallest:
        smallest=i
print(smallest)

largest=a[0]
for i in a:
    if i>largest:
        largest=i

print(largest)
a.sort()
print(a[0],a[len(a)-1])

a=[38,21,53,62,19]
print(min(a),max(a))

# 요소의 합계 구하기
a=[10,10,10,10,10]
x=0
for i in a:
    x+=i

print(x)
print(sum(a))