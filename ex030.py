#문자열
string = 'abcd'
#문자열의 재배치 b를 B로 바꿈
string.replace('b', 'B')
#string 출력
print(string)
#출력결과는 abcd 그대로 나오게 될 것이다.
#이유는 문자열은 변경할 수 없는 자료형이기 때문이다.
#replace를 사용하게 되면 원래의 string은 그대로 두고 새로운 문자열 string을 리턴해준다.
#하지만 현재의 코딩내용에서 replace의 값을 바인딩하지 않기 때문에 변경된 값은 출력되지 않을것이다.