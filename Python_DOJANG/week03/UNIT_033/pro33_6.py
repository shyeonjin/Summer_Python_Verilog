# 심사문제: 키운트다운 함수만들기
# 입력으로 정수 입력
# c를 호출할 떄 마다 숫자가 1씩 즐어들게 만드시오
# 클로저로 완성
def count_down(n):
    i=n+1
    def count():
        nonlocal i
        i-=1
        return i
    return count
n=int(input())
c=count_down(n)
for i in range(n):
    print(c(),end=" ")