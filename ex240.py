def 함수0(num) : # 입력된 값에 2를 곱함
    return num * 2

def 함수1(num) : # 입력된값에 2를 더하고 함수0을 호출하여 대입
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10 #입력된 값에 10을 더함
    return 함수1(num) #함수 1을 호출

c = 함수2(2) 
# 함수2부분에서 2에 10을 더한 값을 num으로 하고 함수1 호출 (현재 num : 12)
# 함수1부분에서 앞에서 구한 값에 2를 더하고 함수0 호출 (현재 num : 14)
# 함수0부분에서 앞에서 구한 값에 2를 곱하고 리턴하여 결과 도출 (현재 num : 28)
print(c)