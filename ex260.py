class OMG :  # 클래스 정의
    def print() :
        print("Oh my god")
		
mystock = OMG() # 객체가 생성, 비어있음
mystock.print()     
# 메서드를 호출한 객체가 해석되는 자리로 넘어가게됨 → OMG.print(mystock)으로 해석하게됨 
# 따라서 인자가 없는 곳에서 인자가 넘어오기 때문에 오류가 일어남
# 위의 정의하는 부분에서 def print(self) : 로 정의하여주면 오류가 일어나지 않을 것이다.