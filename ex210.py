def message1(): #를 실행할 시 A출력
    print("A")

def message2(): #를 실행할 시 B출력
    print("B")

def message3():
    for i in range (3) : #3번 실행
        message2() #B가 출력
        print("C") #C 출력
    message1() #for문이 다 돌아간후 A출력

message3()
#따라서 B C B C B C A가 하나씩 출력된다.