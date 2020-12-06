low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = [] #volatility라는 리스트 생성
for i in range(5): #위의 low와 high리스트의 길이가 모두 5이므로 범위지정
	diff = high_prices[i] - low_prices[i] #변동폭
	volatility.append(diff) #구한 변동폭을 아까 만들어 놓은 volatility리스트에 대입

print(volatility)