import requests
#requests.get을 통해 서버에 요청을 보내 응답을 받는다.
#requests.json을 통해 올린 파일을 요청을 통해 받고 결과값을 파싱(컴퓨터언어를 번역)해준다.
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

#받아 온 값들이 문자열로 되어있으므로 계산을 위해 float함수를 이용하여 숫자로 변환하여준다.
#시가
open = float(btc['opening_price'])

#최고가
high = float(btc['max_price'])

#최저가
low = float(btc['min_price'])

#변동폭 : 최고가에서 최저가를 빼준다.
diff = high - low

# 시가와 변동폭을 더한 값을 먼저 계산 (계산된 값은 튜플)
# 시가와 변동폭의 합이 최고가보다 크면
if (open+diff) > high:
	#"상증장" 출력
	print("상승장")
#크지 않으면
else:
	#"하락장" 출력
	print("하락장")
