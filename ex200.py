ohlc = [["open", "high", "low", "close"],
		[100, 110, 70, 100],
		[200, 210, 180, 190],
		[300, 310, 300, 310]]

# 각 거래일 수익음: 시가 - 종가
# 총 수익금
total_profit = 0
#하루 시가와 종가에서
for day_price in ohlc[1:]:
	profit = day_price[0] - day_price[3] # 수익금 계산
	total_profit += profit #계산한 수익금 누적시킴
	
print(total_profit)