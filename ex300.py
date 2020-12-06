per = ["10.31", "", "8.00"]

for i in per:
	try:
		print(float(i)) # 문자열 숫자로 변환
	except:
		print(0) # 예외가 발생하였을 때 0 출력
	else:
		print("clean data") # 예외가 발생하지 않았을 때 실행됨
	finally:
		print("변환 완료") # 예외 방생 여부 관계없이 코드 실행
#
# 위코드 실행시
#10.31
#clean data
#변환 완료
#0
#변환 완료
#8.00
#clean data
#변환 완료
# 가 출력될 것이다.

