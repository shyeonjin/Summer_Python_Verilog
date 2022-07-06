# 연습문제: 파일에서 10자 이하인 단어 개수 세기
# 단어가 줄 단위로 저장된 word.txt
# 다음 소스 코드를 완성하여 10자 이하인 단어의 개수 출력

lines=['anonymously\n','compatibility\n','dashboard\n',
        'experience\n','photography\n','spotlight\n','warehouse\n']
with open('words.txt','w') as file:
    file.writelines(lines)

with open('words.txt','r') as file:
    count=0
   
    for i in file:
       
        if len(i.strip('\n'))<=10:
            count+=1
    print(count)