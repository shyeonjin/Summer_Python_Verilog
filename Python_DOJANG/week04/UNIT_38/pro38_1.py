# 예외 처리 사용하기

# try except로 사용하기
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except:    
    print('예외가 발생했습니다.')



# 특정 예외만 처리하기
y=[10,20,30]

try:
    index,x=map(int,input('인덱스와 나눌 숫자를 입력하세요:').split())
    print(y[index]/x)
except ZeroDivisionError:    
    print('숫자를 0으로 나눌 수 없습니다.')
except IndexError:           
    print('잘못된 인덱스입니다.')



# 예외의 에러 메시지 받아오기
y = [10, 20, 30]
 
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError as e:                   
    print('숫자를 0으로 나눌 수 없습니다.', e)   
except IndexError as e:
    print('잘못된 인덱스입니다.', e)


