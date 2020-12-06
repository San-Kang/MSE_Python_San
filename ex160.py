리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
#1
#for i in 리스트:
	#변수의 이름에서 끝나는 부분을 확인하여 h와 c확장자 파일 출력
#	if i.endswith(('.h', '.c')):
#		print(i)

#2
for i in 리스트:	
	split = i.split(".") # .을 두고 문자를 나눔
	if (split[1] == "h") or (split[1] == "c"): # . 뒤의 문자가 h와 c인 것을 출력
	print(i)