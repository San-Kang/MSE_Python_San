nums = [1, 2, 3, 4, 5]
#평균을 구하기 위해서는 모든 값을 더한 것에서 값들의 수 만큼 나누면 된다.
#따라서 리스트의 합을 출력해주는 sum과 리스트의 길이를 알려주는 len를 사용한다.
average = sum(nums) / len(nums)
#평균값을 출력해준다.
print(average)