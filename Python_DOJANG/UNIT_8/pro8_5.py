# 심사문제: 합격 여부 출력하기
#국어 90점이상, 영어 80점초과, 수학 85초과, 과학 80점이상 합격
korean,english,mathematics,science=map(int,input().split())
print(korean>=90 and english>80 and mathematics>85 and science>=80)