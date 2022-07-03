# 계단식으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j<=i:
            print("*",end="")
    print()

# 대각선으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j==i:
            print("*",end="")
    print()


for i in range(5):
    for j in range(5):
        if j==i:
            print("*",end="")
        
        else:
            print(" ",end="")
    print()
    