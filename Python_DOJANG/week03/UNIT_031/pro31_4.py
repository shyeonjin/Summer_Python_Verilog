# 연습문제: 재귀호출로 회문 판별하기

def is_palindrome(word):
    if len(word)<2:
        return True
    if word[0] !=word[-1]:
        return False
    
    return is_palindrome(word[1:-1])

print(is_palindrome('hello'))
print(is_palindrome('level'))