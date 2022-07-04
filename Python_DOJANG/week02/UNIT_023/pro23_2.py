# for 반복문을 한 번만 사용하기

a= [[10,20,],[30,40],[50,60]]
for x,y in a:
    print(x,y)

# for 반복문을 두 번 사용하기
for i in a:
    for j in i:
        print(j,end=" ")
    print()

# for와 range 사용하기

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()


# while 반복문을 한 번 사용하기
i=0
while i<len(a):
    x,y=a[i]
    print(x,y)
    i+=1


# while 반복문을 두 번 사용하기
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j],end="")
        j+=1
    print()
    i+=1