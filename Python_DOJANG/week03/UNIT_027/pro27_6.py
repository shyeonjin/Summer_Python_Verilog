# 심사문제: 특정 문자가 들어있느 단어 찾기
# 문자열이 저장된 words2.txt파일이 주어짐
# 문자 c가 포람된 단어를 각 줄에 출력하는 프로그램
# 단어를 출력할 때는 등장한 순서대로 출력해야 함 , .운 츌력X
line='''Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.'''
with open("words2.txt",'w') as file:
    file.write(line)
finl=[]
endl=[]
with open("words2.txt",'r') as file:
    l=None
    while l !='':
        l=file.readline()
        newl=l.split(" ")
        for i in newl:
            if i.count('c')!=0:
                finl.append(i)
    for f in finl:
        endl.append(f.strip(',.'))
    for e in endl:
        print(e)
