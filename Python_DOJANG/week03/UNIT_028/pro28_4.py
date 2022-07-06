# 심사문제: 파일에서 회문인 단어 출력하기
# 단어가 줄단위로 저장된 word.txt파일
# 회문이 단어 출력
lines=['apache\n','decal\n','did\n','neep\n','noon\n','refer\n','river\n']
with open('word.txt','w') as file:
    for i in lines:
        file.write(i)
new=[]
with open('word.txt','r') as rfile:
    for i in rfile:
        new.append(i.strip("\n"))
    for n in new:
        if n==n[::-1]:
            print(n)