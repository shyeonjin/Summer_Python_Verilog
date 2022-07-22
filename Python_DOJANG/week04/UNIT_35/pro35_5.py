# 연습문제: 날짜 클래스 만들기
# Date클래스를 만들고 is_date_vaild는 문자열이 올바른 날짜인지 검사하는 메서드 입니다.
# 월은 12월깢 일은 31일까지 있어야한다.

class Date:
    @staticmethod
    def is_date_vaild(data):
        y,m,d=map(int,data.split("-"))
        return m<13 and d<32

        


if Date.is_date_vaild('2000-10-31'):
    print("올바른 날짜 형식입니다")
else:
    print("잘못된 날짜 형식입니다")