# 연습문제 : 파일 예외 처리하기
try:
    file = open('maria.txt', 'r')
except FileNotFoundError:                       
    print('파일이 없습니다.')
else:
    s = file.read()
    file.close()