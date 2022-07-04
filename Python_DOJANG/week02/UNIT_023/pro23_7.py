# 심화문제: 지뢰찾기
# 표준 입력 2차원 가로 세로가 입력 다음줄부터 요소로 들어갈 문자 입력
# 2차원 리스에서 *는 지뢰이고 .은 아니다 지뢰가 아닌 요소에는 인접한 지뢰의
# 개수를 출력하는 프로그램을 만드시오

col,row= map(int,input("가로 세로 입력:").split())

fin=[ [0 for i in range(col)]for j in range(row)]
matrix=[]
for i in range(row):
    matrix.append(list(input()))

x=[-1,0,1,-1,1,-1,0,1] # 가로
y=[-1,-1,-1,0,0,1,1,1] # 세로     
count=0

for i in range(row):
    for j in range(col):
        if matrix[i][j]=="*":
            fin[i][j]="*"
        # 주위가 8개 -1-1/0-1/1-1/-10/(00)기준/10/-11/01/11 
        else:
            # 주위 8개 
            for k in range(8):
                if 0<= j+x[k]<col and 0<=i+y[k]<row:
                    if matrix[i+y[k]][j+x[k]]=="*":
                        count+=1
            fin[i][j]=count
            count=0
    

for i in range(row):
    for j in range(col):
        print(fin[i][j], end='')
    print()