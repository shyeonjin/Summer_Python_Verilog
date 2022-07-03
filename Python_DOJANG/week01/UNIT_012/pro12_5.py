# 심사문제: 딕셔너리에 게임 캐릭터 능력치 저장
# 입력 첫 번째 줄은 키, 두 번째 줄은 값을 넣는 딕셔너리 생성

first_k=input("").split()
second_T=map(float,input("").split())
print(dict(zip(first_k,second_T)))