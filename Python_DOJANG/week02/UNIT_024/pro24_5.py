# 심사문제: 특정 단어 개수 세기
# 문자열을 입력받는다. 문자열에서 the의 개수를 출력하는 프로그램
# them, eher,their은 포함하지 않는다
sentence=input("문장을 입력하세요")
listsen=sentence.split()
print(listsen.count("the"))