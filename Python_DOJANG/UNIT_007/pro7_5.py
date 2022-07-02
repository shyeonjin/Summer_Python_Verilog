# 심사문제: 날짜와 시간 출력하기
# 입력된 날짜와 시간을 년-월-일T시:분:초 형식으로 출력되게 만드세요
y,m,d,h,m,s=input().split()
print(y,m,d,sep="/",end="T")
print(h,m,s,sep=":")