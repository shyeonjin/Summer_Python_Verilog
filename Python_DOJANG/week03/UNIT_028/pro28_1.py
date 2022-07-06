# 회문 판별하기

# 반복문으로 문자 검사하기
word=input('단어를 입력하세요: ')

is_palindrome=True
for i in range(len(word)//2):
    if word[i] != word[-1 -i]:
        is_palindrome=False
        break

print(is_palindrome)


# 시퀀스 뒤집기로 문자 검사하기
word=input('단어를 입력하세요:')

print(word==word[::-1])

# 리스트와 reversed 사용하기
word='level'
print(list(word)==list(reversed(word)))


# 문자열의 join 메서드와 reversed 사용하기
word='level'
print(''.join(reversed(word)))


