# 서식 지정자로 문자열 넣기
print("I am %s" %'james')


name='maria'
print("I am %s" %name)

# 서식 지정자로 숫자 넣기
print("I am %d years old."%20)

# 서식 지정자로 소수점 표현하기
print("%f"%2.3)
print("%.2f"%2.3)
print("%.3f"%2.3)

# 서식 지정자로 문자열 정렬하기
print ("%10s"%"Python")

print("%10d"%150)
print("%10d"%15000)

print("%10.2f"%2.3)
print("%10.2f"%2000.3)

# 왼쪽정렬
print("%-10s"%"Python")



# 서식 지정자로 문자열 안에 값 여러개 넣기
print("Today is %d %s."%(3,'April'))
print("Today is %d%s."%(3,'April'))


# format 메서드 사용하기

print("Hello,{0}".format('world'))
print("Hello,{0}".format(100))

# format 메서드로 값을 여러 개 넣기
print("Hello,{0}{2}{1}".format('Python','Script',3.6))

# format 메서드로 같은 값을 여러 개 넣기

print('{0} {0} {1} {1}'.format('Python','Script'))

# format 메서드에서 인덱스 생략하기
print("Hello {} {} {}".format('Python','Script',3.6))

# format 메서드에서 인덱스 대신 이름 지정하기
print("Hello {language} {version} ".format(language='Python',version=3.6))

# 문자열 포매팅에 변수를 그대로 사용하기
language='Python'
version=3.6
print(f"Hello,{language} {version}")

# format 메서드로 문자열 정렬하기
print("{0:<10}".format('Python'))
print("{0:>10}".format('Python'))

# 숫자 개수 맞추기
print("%03d"%1)
print("{0:03d}".format(35))

print("%08.2f"%3.6)
print("{0:08.2f}".format(150.37))

# 채우기와 정렬을 조합해서 사용하기
print("{0:0<10}".format(15))

print("{0:0>10}".format(15))

print("{0:0>10.2f}".format(15))
print("{0: >10}".format(15))
print("{0:>10}".format(15))
print("{0:x>10}".format(15))

# 금액에서 천단위로 콤마 넣기
print(format(1493500,","))
print("%20s".format(1493500,","))
print('{0:,}'.format(1493500))
print("{0:>20,}".format(1493500))

print("{0:0>20,}".format(1493500))