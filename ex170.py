#초기값을 1로 설정
result = 1
#반복할 범위를 정함 1부터 11이전(10까지)
for i in range(1, 11) :
	result *= i # result = result * i 를 축약함 이를 통해 값은 계속 곱해진다.
print(result)