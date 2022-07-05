# 심사문제: 딕셔너리에서 특정 값 삭제하기
# 표준 입력으로 문자열 여러 개와 숫자 여러개가 두 줄로 입력
# 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성
# 키가 'delta'인 키-값 쌍과 값이 30인 키-값 쌍을 삭제 출력
first=input("문자열을 입력하세요")
second=input("숫자를 입력하세요")
first=first.split(" ")
second=map(int,second.split(" "))
dic=dict(zip(first,second))
dic={key: value for key,value in dic.items() if value !=30 if key !='delta'}
print(dic)