# 파일에 문자열 쓰기, 읽기
# 파일에 문자열 쓰기

file=open("hello.txt","w")
file.write('hello,world!')
file.close()


# 파일에서 문자열 읽기
file=open('hello.txt','r')
s=file.read()
print(s)
file.close()

# 자동으로 파일 객체 닫기
with open('hello.txt','r') as file:
    s=file.read()
    print(s)