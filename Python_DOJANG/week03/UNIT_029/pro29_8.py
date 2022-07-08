# 심사문제: 사칙 연산 함수 만들기
# 표준 입력 숫자 두 개 입력
# 두 숫자 덧셈, 뺄셈, 곱셈, 나눗셈의 결과 츌력 나눗셈의 결과는 실수
def all_cal(a,b):
    return a+b, a-b, a*b, a/b



first,second=map(int,input("숫자를 입력하세요").split())
add,sub,mul,div=all_cal(first,second)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(add,sub,mul,div))