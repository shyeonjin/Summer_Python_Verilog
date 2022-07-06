# N-gram 만들기
# N글자 출력

text='Hello'
for i in range(len(text)-1):
    print(text[i],text[i+1],sep="")

text='this is python script'
words=text.split()

for i in range(len(words)-1):
    print(words[i],words[i+1])


# zip으로 2-gram 만들기
text='hello'

two_gram=zip(text,text[1:])
for i in two_gram:
    print(i[0],i[1],sep='')


print(list(zip(text,text[1:])))

text='this is python script'
words=text.split()
print(list(zip(words,words[1:])))

# zip과 리스트 표현식으로 N-gram 만들기
text='hello'
print([text[i:] for i in range(3)])
print(list(zip(['hello','ello','llo'])))
print(list(zip(*['hello','ello','llo'])))
print(list(zip(*[text[i:]for i in range(3)])))