# 연습문제: 공배수 구하기
# 1~100까지 숫자 중 3과 5의 공배수를 세트형태로 출력
a={i for i in range(1,101) if i%3==0}
b={i for i in range(1,101) if i%5==0}
print(a&b)