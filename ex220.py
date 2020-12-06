def print_max(a, b, c) :
	max_val = 0
	if a > max_val : #a가 max_val보다 크면 a를 max_val값으로 한다.
		max_val = a
	elif b > max_val : #b가 max_val보다 크면 b를 max_val값으로 한다. (a와 max_val의 비교 후)
		max_val = b
	elif c > max_val : #c가 max_val보다 크면 c를 max_val값으로 한다. (a,b와 max_val의 비교 후)
		max_val = c
	print(max_val)

print_max(100, 89, 220) #가장 큰 수인 220이 출력된다.