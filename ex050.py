data = "039490		"
#오른쪽 공백을 제거하는 메서드인 rstrip을 사용하면된다.
#rstrip은 strip메서드처럼 기존의 값을 두고 새로운 변경값을 내주기 때문에
#새로바인딩을 해야한다.
data = data.rstrip()
#변경된 값을 확인하고 싶으면 출력하여보면된다.
print(data)
