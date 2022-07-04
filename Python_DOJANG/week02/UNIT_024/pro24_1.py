# 문자열 바꾸기
print("hello world!".replace("world","Python"))

# 문자 바꾸기
table=str.maketrans('aeiou','12345')
print('apple'.translate(table))

# 문자열 분리하기
print("apple pear grape pinapple orange".split())

print("apple,pear,grape,pinapple,orange".split(","))

# 구분자 문자열과 문자열 리스트 연결하기
print(" ".join(['apple','pear','grape','pineapple','orange']))

print("-".join(['apple','pear','grape','pineapple','orange']))


# 소문자를 대문자로 바꾸기
print('python'.upper())

# 대문자를 소문자로 바꾸기
print("PYTHON".lower())

# 왼쪽 공백 삭제하기
print("      Python      ".lstrip())

# 오른쪽 공백 삭제하기
print("      Python      ".rstrip())

# 양쪽 공백 삭제하기
print("      Python      ".strip())

# 왼쪽 특정 문자 삭제하기
print(",python.".lstrip(",."))

# 오른쪽 특정 문자 삭제하기
print(",python.".rstrip(",."))

# 양쪽 특정 문자 삭제하기
print(",python.".strip(",."))

# 문자열을 왼쪽 정렬하기
print("python".ljust(10))


# 문자열을 오른쪽 정렬하기
print("python".rjust(10))

# 문자열을 가운데 정렬하기
print("python".center(10))


# 메서드 체이닝
print("python".rjust(10).upper())


# 문자열 왼쪽에 0 채우기
print("35".zfill(4))
print("3.5".zfill(6))
print("Hello".zfill(10))

# 문자열 위치 찾기
print("apple pineapple".find("pl"))
print("apple pineapple".find("xy")) # 없으면 -1

# 오른쪽에서부터 문자열 위치 찾기
print("apple pineapple".rfind("pl"))
print("apple pineapple".rfind("xy")) # 없으면 -1

# 문자열 위치 찾기
print("apple pineapple".index("pl"))

# 오른쪽에서부터 문자열 위치 찾기
print("apple pineapple".rindex("pl"))

# 문자열 개수 세기
print("apple pineapple".count("pl"))
