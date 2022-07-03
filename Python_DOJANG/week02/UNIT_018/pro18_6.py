# 심사문제: 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
# 표준입력으로 정수가 두 개 입력 (첫 번째 값=1~200, 두 번째 값=10~200)
# 첫 번째 값은 무조건 두 번째 값보다 작다.
# 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력
first,second=map(int,input("숫자를 입력하시오").split())

for i in range(first,second+1):
    if i %10==3:
        continue
    print(i,end=" ")
