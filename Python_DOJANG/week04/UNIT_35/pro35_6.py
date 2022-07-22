# 심사문제: 시간 클래스 만들기
# 표준 입력응로 시:분:초 입력
# Time 클래스를 완성하고 시,분,초가 출력되게 만드세요
# is_time_vaild는 문자열이 올바른 시간인지 검사하는 메서드 
# 시간은 24시까지, 분은 59분, 초는 60초까지
class Time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
    
    @staticmethod
    def is_time_vaild(data):
        h,m,s=map(int,data.split(":"))
        return h <25 and m <60 and s<61

    @classmethod
    def from_string(cls,data):
        h,m,s=map(int,data.split(":"))
        return cls(h,m,s)

time_string=input()

if Time.is_time_vaild(time_string):
    t=Time.from_string(time_string)
    print(t.hour,t.minute,t.second)
else:
    print("잘못된 시간 형식입니다.")