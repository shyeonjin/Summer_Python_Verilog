# 심사문제: 합격 여부 판단
# 국어, 영어, 수학, 과학 점수를 입력받고
# 평균이 80이상이면 합격 0~100의 점수가 안들어온다면 
# 잘못된 점수 출력
mean=0
korean,english,mathematics,science=map(int,input("국어, 영어, 수학, 과학 점수입력: ").split())
if 0<=korean<=100 and 0<=english<=100 and 0<=mathematics<=100 and 0<=science<=100:
    mean=(korean+english+mathematics+science)/4
    if mean >= 80:
        print("합격입니다.")
    else: 
        print("불합격입니다")
else:
    print("잘못된 점수")
