# Stock 클래스 생성
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name # 객체인자를 생성하여 클래스의 name을 바인딩
        self.code = code # 객체인자를 생성하여 클래스의 code를 바인딩
        self.per = per # 객체인자를 생성하여 클래스의 per을 바인딩
        self.pbr = pbr # 객체인자를 생성하여 클래스의 pbr을 바인딩
        self.dividend = dividend # 객체인자를 생성하여 클래스의 dividend를 바인딩

종목 = [] # 종목이라는 리스트 생성

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
	print(i.code, i.per)    # i -> Stock 클래스의 객체를 바인딩함