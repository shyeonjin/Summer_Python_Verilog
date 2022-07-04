# 심사문제: 2의 거듭제곱 리스트 생성하기
# 표준입력 2개 입력 첫 번째(1~20) < 두 번째(10~30)
# 첫 번째 정수부터 두 번째 정수까지를 지수로 하는 2의 거듭제곱 리스트를 
# 출력하는 프로그램을 만드세요
first,second= map(int,input("정수를 입력하세요: ").split())

answer=[2**i for i in range(first,second+1)]
answer.pop(1)
answer.pop(len(answer)-2)
print(answer)