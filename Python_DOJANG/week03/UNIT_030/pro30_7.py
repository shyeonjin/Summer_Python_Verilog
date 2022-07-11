# 심화문제: 가장 낮은 점수,높은 점수와 평균 점수를 구하는 함수 만들기
# 입력으로 국어, 영어, 수학, 과학 점수 입력
# 가장 높은 점수, 가장 낮은 점수, 평균 점수 출력, 평균은 실수

korean,english,mathematics,science=map(int,input("점수를 입력하세요").split())
def get_min_max_score(*args):
    return min(args),max(args)


def get_average(**args):
    t=0
    for i in args.values():
        t+=i
    return t/len(args)


min_score,max_score=get_min_max_score(korean,english,mathematics,science)
average_score=get_average(korean=korean,english=english,mathematics=mathematics,science=science)
print("낮은 점수:{0:.2f} ,높은 점수: {1:.2f} ,평균 점수:{2:.2f}".format(min_score,max_score,average_score))


min_score,max_score=get_min_max_score(english,science)
average_score=get_average(english=english,science=science)
print("낮은 점수:{0:.2f} ,높은 점수: {1:.2f} ,평균 점수:{2:.2f}".format(min_score,max_score,average_score))