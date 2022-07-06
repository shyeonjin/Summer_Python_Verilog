# 연습문제: 단어 단위 N-gram 만들기
# 표준 입력으로 정수와 문자열이 각 줄에 입력
# N-gram을 튜플로 출력
# 입ㄺ된 문자열의 단어 개수가 입력된 정수 미만이라면 'wrong'출력
n=int(input())
text=input()
words=text.split()
if len(words)<n:
    print('wrong')
else:
    n_gram=zip(*[words[i:] for i in range(n)])
    for i in n_gram:
        print(i)