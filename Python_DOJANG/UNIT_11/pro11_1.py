# 특정 값이 있는지 확인하기

a=[0,10,20,30,40,50,60,70,80,90]
print(30 in a)
print(100 in a)
print(100 not in a)
print(30 not in a)
print(43 in (38,76,43,62,19))
print(1 in range(10))
print('P' in 'Hello,Python')

a=[]

# 시퀀스 객체 연결하기
a=[0,10,20,30]
b=[9,8,7,6]
print(a+b)
print(list(range(0,10))+list(range(10,20)))
print(tuple(range(0,10))+tuple(range(10,20)))
print("Hello,"+"world!")

# 시퀀스 객체 반복하기
print([0,10,20,30]*3)
print(list(range(0,5,2))*3)
print(tuple(range(0,5,2))*3)
print("Hello"*3)