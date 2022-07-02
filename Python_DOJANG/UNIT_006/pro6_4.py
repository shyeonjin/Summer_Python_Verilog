# 입력 값을 변수 두 개에 저장하기
a,b=input("문자열 두 개를 입력하세요").split()
print(a);print(b)

# 두 숫자의 합 구하기
a,b=input("숫자 두 개를 입력하세요").split()
print(a+b)

# 입력 값을 정수로 변환하기
a,b=input("숫자 두 개를 입력하세요:").split()
a=int(a);b=int(b)
print(a+b)

# map을 사용하여 정수로 변환하기
a,b = map(int, input('숫자 두 개를 입력하세요: ').split())
print(a + b)

# 입력받은 값을 콤마를 기준으로 분리하기
a,b=map(int,input("숫자 두 개를 입력하세요(콤마 사용):").split(','))
print(a+b)
