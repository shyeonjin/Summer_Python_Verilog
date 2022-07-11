# 심사문제: 파일 이름을 한꺼번에 바꾸기
# 표준 입력으로 숫자.확장자 형식으로 된 파일 여러 개가 입력
# 파일이름이 숫자 3개이면서 앞에 0이 들어가는 형식으로 출력


files=input().split()
print(list(map(lambda x:'{0:03d}'.format(int(x.split('.')[0]))+'.'+x.split('.')[1],files)))